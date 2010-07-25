from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from flickrpayments.views import photo_list

urlpatterns = patterns('',
    url(r'^$', photo_list, name='sitewide_index',),
    
)
