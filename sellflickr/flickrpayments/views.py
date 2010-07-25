
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.list_detail import object_detail, object_list
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from paypal.standard.ipn.forms import PayPalIPNForm
from paypal.standard.ipn.models import PayPalIPN
from paypal.standard.forms import PayPalPaymentsForm

from flickrimporter.models import FlickrPhoto
from flickrpayments.models import Payment, UserPaypal
from flickrpayments.forms import FlickrPaymentForm
from django.views.generic.simple import direct_to_template

def photo_list(request):
    if request.mainsite:
        return direct_to_template(request,template='homepage.html')
    elif request.subdomain:
        photos = FlickrPhoto.objects.filter(owner__user=request.subdomain.user)
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
    # request.session['payment_obj'] = payment_obj
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


@require_POST
def ipn(request, item_check_callable=None):
    """
    PayPal IPN endpoint (notify_url).
    Used by both PayPal Payments Pro and Payments Standard to confirm transactions.
    http://tinyurl.com/d9vu9d
    
    PayPal IPN Simulator:
    https://developer.paypal.com/cgi-bin/devscr?cmd=_ipn-link-session
    """
    # from the paypal invoice get
    # payment obj (inovice number == payment obj pk)
    # get the buyer email

    # save the amount and paypal_txn_key to 
    # payment object and activate the 
    # payment obj
    
    # from payment obj get photo
    # mail the photo originla url to buyer
    
    flag = None
    ipn_obj = None
    form = PayPalIPNForm(request.POST)
    if form.is_valid():
        try:
            ipn_obj = form.save(commit=False)
        except Exception, e:
            flag = "Exception while processing. (%s)" % e
    else:
        flag = "Invalid form. (%s)" % form.errors

    if ipn_obj is None:
        ipn_obj = PayPalIPN()    

    ipn_obj.initialize(request)

    if flag is not None:
        ipn_obj.set_flag(flag)
    else:
        # Secrets should only be used over SSL.
        if request.is_secure() and 'secret' in request.GET:
            ipn_obj.verify_secret(form, request.GET['secret'])
        else:
            ipn_obj.verify(item_check_callable)

    ipn_obj.save()
    return HttpResponse("OKAY")


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
    owner = request.user.flickruser_set.all()[0]
    subdomain = owner.subdomain
    return redirect(subdomain)

@login_required
def my_config(request):
    subdomain = request.user.flickruser_set.get().subdomain
    return redirect(subdomain.get_config_url())
    