
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.list_detail import object_detail, object_list
from django.views.decorators.csrf import csrf_exempt

from paypal.standard.forms import PayPalPaymentsForm

from flickrimporter.models import FlickrPhoto
from flickrpayments.models import Payment, UserPaypal
from flickrpayments.forms import FlickrPaymentForm

def photo_list(request):
    # photos = FlickrPhoto.objects.filter(owner__user=request.subdomain.user)
    photos = FlickrPhoto.objects.filter(owner__user=request.user)
    return object_list(request, photos, template_name='flickrpayments/photo_list.html')

def get_subdomain_user(request):
    "temp fix" 
    try:
        return request.subdomain.user
    except AttributeError:
        return request.user

def photo_detail(request, object_id):
    photo = get_object_or_404(FlickrPhoto, pk=object_id, owner__user=get_subdomain_user(request))
    photos = FlickrPhoto.objects.filter(owner__user=get_subdomain_user(request))
    user_paypal = UserPaypal.objects.get(user=get_subdomain_user(request))
    payment_obj = Payment.objects.create(photo=photo)
    notify_url = request.build_absolute_uri(reverse('paypal-ipn'))
    return_url = request.build_absolute_uri(reverse('flickrpayments_buy_done', args=[object_id]))
    cancel_return = request.build_absolute_uri(request.get_full_path())
    paypal_dict = {
        "business": user_paypal.email,
        "amount": photo.get_price,
        "item_name": 'payment for photo %s with invoice %s' % (photo.title, payment_obj.pk),
        "invoice": payment_obj.pk,
        "notify_url": notify_url,
        "return_url": return_url,
        "cancel_return": cancel_return,
    }
    print paypal_dict
    is_debug = settings.DEBUG
    form = PayPalPaymentsForm(initial=paypal_dict)
    return object_detail(request, 
                         photos, 
                         object_id=object_id, 
                         template_name='flickrpayments/photo_detail.html', 
                         extra_context={'photo_list': photos.order_by('?')[:6],
                                        'form': form,
                                        'is_debug': is_debug})

@csrf_exempt
def buy_done(request, object_id):
    photo = get_object_or_404(FlickrPhoto, pk=object_id, owner__user=get_subdomain_user(request))
    photos = FlickrPhoto.objects.filter(owner__user=get_subdomain_user(request))
    return render_to_response('flickrpayments/buy_done.html', 
                              {'photo': photo, 
                               'photo_list': photos},
                              context_instance=RequestContext(request))


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

from django.shortcuts import redirect

@login_required
def my_site(request):
    subdomain = request.user.flickruser_set.get().subdomain
    return redirect(subdomain)

@login_required
def my_config(request):
    subdomain = request.user.flickruser_set.get().subdomain
    return redirect(subdomain.get_config_url())
    