
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.list_detail import object_detail, object_list

from flickrimporter.models import FlickrPhoto
from flickrpayments.forms import FlickrPaymentForm

def photo_list(request):
    # photos = FlickrPhoto.objects.filter(owner__user=request.subdomain.user)
    photos = FlickrPhoto.objects.filter(owner__user=request.user)
    return object_list(request, photos, template_name='flickrpayments/photo_list.html')


def photo_detail(request, object_id):
    # photos = get_object_or_404(FlickrPhoto, pk=object_id, owner__user=request.subdomain.user)
    photos = get_object_or_404(FlickrPhoto, pk=object_id, owner__user=request.user)
    return object_list(request, photos, template_name='flickrpayments/photo_detail.html')


def buy_photo(request, object_id):
    photos = get_object_or_404(FlickrPhoto, pk=object_id, owner__user=request.user)
    

@login_required
def set_price(request):
    queryset = FlickrPhoto.objects.filter(owner__user=request.user)
    FormSet =  modelformset_factory(FlickrPhoto, form=FlickrPaymentForm)
    if request.method == 'POST':
        form = FormSet(request.POST, queryset=queryset)
    else:
        form = FormSet(queryset=queryset)
    return render_to_response('flickrpayments/set_price.html', 
                              {'form': form},
                              context_instance=RequestContext(request))
