from django.conf.urls.defaults import *

urlpatterns = patterns('flickrpayments.views',
    url(r'^set-price/$', 'set_price', name='flickrpayments_set_price'),
    url('^detail/(?P<object_id>\d+)/$', 'photo_detail', name='flickrpayments_photo_detail'),
    url('^buy/(?P<object_id>\d+)/$', 'buy_photo', name='flickrpayments_photo_buy'),
    url('^buy/done/(?P<object_id>\d+)/$', 'buy_done', name='flickrpayments_buy_done'),
    url('^myconfig/$', 'my_config', name='admin_configure'),
    url('^mysite/$', 'my_site', name='my_site'),
    url('^$', 'photo_list', name='flickrpayments_photo_list'),
)

urlpatterns += patterns('',
    url('^ipn/', include('paypal.standard.ipn.urls')),
)
