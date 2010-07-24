import flickrapi

from django.conf import settings

from flickrimporter.models import FlickrUser
from django.contrib.auth.models import User

class FlickrBackend(object):
    def authenticate(self, flickr_token):
        try:
            fuser = FlickrUser.objects.get(token = flickr_token)
            return fuser.user
        except FlickrUser.DoesNotExist:
            #We have a token. Check if we can create a useruser with the given token.
            flickr = flickrapi.FlickrAPI(settings.FLICKR_API_KEY,
               settings.FLICKR_API_SECRET, token=flickr_token,
               store_token=False)
            try:
                flickr.auth_checkToken()
            except flickrapi.FlickrError:
                return None
            #Todo get username etc
            username = User.objects.count() + 1
            user = User.objects.create(username = username)
            FlickrUser.objects.create(user=user, token = flickr_token)
            return user
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except:
            return None
            

