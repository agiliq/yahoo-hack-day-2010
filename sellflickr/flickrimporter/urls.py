from django.conf.urls.defaults import *

urlpatterns = patterns('flickrimporter.views',
    url(r'^login/$', 'content', name="flickrimporter_index"),
    url(r'^login/done/$', 'callback'),
)
