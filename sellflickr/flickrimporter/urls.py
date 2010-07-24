from django.conf.urls.defaults import *

urlpatterns = patterns('flickrimporter.views',
    url(r'^$', 'content', name="flickrimporter_index"),
    url(r'^login/start/$', 'flickr_login_start', name="flickrimporter_index_start"),
    url(r'^login/done/$', 'flickr_login_done'),
)
