import flickrapi

from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from models import FlickrPhoto, FlickrUser

import simplejson
import logging
logging.basicConfig()

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

def require_flickr_auth(view):
    '''View decorator, redirects users to Flickr when no valid
    authentication token is available.
    '''

    def protected_view(request, *args, **kwargs):
        if 'token' in request.session:
            token = request.session['token']
            log.info('Getting token from session: %s' % token)
        else:
            token = None
            log.info('No token in session')

        f = flickrapi.FlickrAPI(settings.FLICKR_API_KEY,
               settings.FLICKR_API_SECRET, token=token,
               store_token=False)

        if token:
            # We have a token, but it might not be valid
            log.info('Verifying token')
            try:
                f.auth_checkToken()
            except flickrapi.FlickrError:
                token = None
                del request.session['token']

        if not token:
            # No valid token, so redirect to Flickr
            log.info('Redirecting user to Flickr to get frob')
            url = f.web_login_url(perms='read')
            return HttpResponseRedirect(url)

        # If the token is valid, we can call the decorated view.
        log.info('Token is valid')

        return view(request, *args, **kwargs)
            

    return protected_view

def flickr_login_start(request):
    flickr = flickrapi.FlickrAPI(settings.FLICKR_API_KEY,
               settings.FLICKR_API_SECRET,)
    url = flickr.web_login_url(perms='read')
    return HttpResponseRedirect(url)

def flickr_login_done(request):
    log.info('We got a callback from Flickr, store the token')
    f = flickrapi.FlickrAPI(settings.FLICKR_API_KEY, 
                            settings.FLICKR_API_SECRET)
    frob = request.GET['frob']
    token = f.get_token(frob)
    from django.contrib.auth import authenticate, login
    user = authenticate(flickr_token = token)
    if user:
        login(request, user)
        return HttpResponseRedirect(reverse("flickrimporter_index"))
    else:
        #Not a valid user
        #Todo do something better.
        return HttpResponse("Flickr failure.")
        
        

@login_required
def content(request):
    f = flickrapi.FlickrAPI(settings.FLICKR_API_KEY, 
                            settings.FLICKR_API_SECRET)
    
    result_json = f.photos_search(user_id='me', per_page='500', format='json')
    parsed_json = simplejson.loads(result_json[14:-1])
    for photo in parsed_json['photos']['photo']:
        flickr_photo = FlickrPhoto()
        flickr_photo.flickr_id = photo['id']
        flickr_photo.secret = photo['secret']
        flickr_photo.server = photo['server']
        flickr_photo.title = photo['title']
        #stub
        flickr_photo.owner = request.user.flickruser_set.get()
        flickr_photo.farm = photo['farm']
        flickr_photo.save()
        
    var = {'total': parsed_json['photos']['total']}
    return render_to_response('flickrimporter/index.html', var)