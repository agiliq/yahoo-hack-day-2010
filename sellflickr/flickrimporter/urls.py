from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('flickrimporter.views',
    url(r'^$', 'content', name="flickrimporter_index"),
    url(r'^import/$', direct_to_template, {'template':'flickrimporter/import.html'}, name="flickr_import"),
    url(r'^login/start/$', 'flickr_login_start', name="flickrimporter_index_start"),
    url(r'^login/done/$', 'flickr_login_done'),
)
