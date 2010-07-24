
from django import forms

from flickrimporter.models import FlickrPhoto

class FlickrPaymentForm(forms.ModelForm):
    
    class Meta:
        model = FlickrPhoto
        fields = ('price',)
    