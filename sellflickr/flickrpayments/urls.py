from django.conf.urls.defaults import *


urlpatterns = patterns('flickrpayments.views',
    url(r'^set-price/$', 'set_price', name='flickrpayments_set_price')
)
