from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('flickrpayments.views',
    url(r'^set-price/$', 'set_price', name='flickrpayments_set_price'),
    url('^detail/(?P<object_id>\d+)/$', 'photo_detail', name='flickrpayments_photo_detail'),
    url('^buy/(?P<object_id>\d+)/$', 'buy_photo_paypal', name='flickrpayments_photo_buy_paypal'),
    url('^buy/done/(?P<object_id>\d+)/$', 'buy_done', name='flickrpayments_buy_done'),
    url('^myconfig/$', 'my_config', name='admin_configure'),
    url('^mysite/$', 'my_site', name='my_site'),
    url('^paypal/$', 'paypal_config', name='flickrpayments_paypal_config'),
    url('^paypal/done/$', direct_to_template,
        {'template': "flickrpayments/paypal_config_done.html"},
        name='flickrpayments_paypal_config_done'),
    url('^$', 'photo_list', name='flickrpayments_photo_list'),
    url('^ipn/$', 'ipn', name="paypal-ipn"),
)

urlpatterns += patterns('',
    # url('^ipn/', include('paypal.standard.ipn.urls')),
    # url('^ipn/$', 'ipn', name="paypal-ipn"),
)
