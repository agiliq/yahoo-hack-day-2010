from django.conf.urls.defaults import *

urlpatterns = patterns('flickrpayments.views',
    url(r'^set-price/$', 'set_price', name='flickrpayments_set_price'),
    url('^list/$', 'photo_list', name='flickrpayments_photo_list'),
    url('^detail/(?P<object_id>\d+)/$', 'photo_detail', name='flickrpayments_photo_detail'),
    url('^buy/(?P<object_id>\d+)/$', 'buy_photo', name='flickrpayments_photo_buy'),
    url('^buy/done/(?P<object_id>\d+)/$', 'buy_done', name='flickrpayments_buy_done'),
)

urlpatterns += patterns('',
    url('^ipn/', include('paypal.standard.ipn.urls')),
)
