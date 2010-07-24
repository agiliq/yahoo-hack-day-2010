
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from django.template import RequestContext

from flickrimporter.models import FlickrPhoto
from flickrpayments.forms import FlickrPaymentForm

def set_price(request):
    queryset = None#FlickrPhoto.objects.filter(owner__user=request.user)
    FormSet =  modelformset_factory(FlickrPhoto, form=FlickrPaymentForm)
    if request.method == 'POST':
        form = FormSet(request.POST, queryset=queryset)
    else:
        form = FormSet(queryset=queryset)
    return render_to_response('flickrpayments/set_price.html', 
                              {'form': form},
                              context_instance=RequestContext(request))
