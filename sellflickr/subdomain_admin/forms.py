from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django import forms
from subdomains.models import Subdomain

class SubdomainUserForm(UserCreationForm):
    subdomain_title = forms.CharField(max_length=50,label='Site name')
    
    def clean(self):
        subdomain_value = self.cleaned_data['username']
        if subdomain_value=='www':
            raise forms.ValidationError('This subdomain cannot be registered')
        try:
            Subdomain.objects.get(subdomain_text=subdomain_value)
        except Subdomain.DoesNotExist:
            return self.cleaned_data
        raise forms.ValidationError('This subdomain is already registered')
    
    def save(self,**kwargs):
        user = super(SubdomainUserForm,self).save(**kwargs)
        user.is_staff=True
        group = Group.objects.get(name='SubUser')
        user.groups.add(group)
        user.save()
        cd = self.cleaned_data
        username, password = cd['username'], cd['password2']
        subdomain = Subdomain.objects.register_new_subdomain(subdomain_text = cd['username'],
                                                             name = cd['subdomain_title'],
                                                             description = "Descriptions",
                                                             user = user)
        subdomain.save()
        # auto_create_menus(subdomain,user)
        return username, password, subdomain
    
class FlickrimportedForm(forms.Form):
    subdomain = forms.CharField(max_length=50,label='Site name',help_text='.flickrcommerce.com')
    
    def clean_subdomain(self):
        sd = self.cleaned_data['subdomain']
        if subdomain_value=='www':
            raise forms.ValidationError('This subdomain cannot be registered')
        try:
            Subdomain.objects.get(subdomain_text=subdomain_value)
        except Subdomain.DoesNotExist:
            return sd
        raise forms.ValidationError('This subdomain is already registered')

    
class DomainNameForm(forms.Form):
    domain_name = forms.CharField(max_length=50,label='Site name',help_text='Point your site to 173.230.152.104')
    default_price = forms.IntegerField()
    