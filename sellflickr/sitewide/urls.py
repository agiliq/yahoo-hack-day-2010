from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {"template": "sitewide/index.html"}, name='sitewide_index',),
    
)
