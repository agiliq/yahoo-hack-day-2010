from django.conf.urls.defaults import *

urlpatterns = patterns('flickrpayments.views',
    url(r'^set-price/$', 'set_price', name='flickrpayments_set_price'),
    url('^list/$', 'photo_list', name='flickrpayments_photo_list'),
    url('^detail/(?P<object_id>)/$', 'photo_detail', name='flickrpayments_photo_detail'),
    url('^buy/(?P<object_id>)/$', 'buy_photo', name='flickrpayments_photo_buy'),
)
