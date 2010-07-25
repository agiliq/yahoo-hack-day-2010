
from django import forms

from flickrimporter.models import FlickrPhoto
from flickrpayments.models import UserPaypal

class FlickrPaymentForm(forms.ModelForm):
    
    class Meta:
        model = FlickrPhoto
        fields = ('price',)
    
    
class PaypalConfigForm(forms.ModelForm):
    class Meta:
        model = UserPaypal
        fields = ("email", )
        