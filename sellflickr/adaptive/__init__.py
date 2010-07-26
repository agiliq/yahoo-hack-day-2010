def get_adaptive_payment_url(returnUrl, cancelUrl, receiverList, **kwargs):
    from django.conf import settings
    API_END_POINT = 'https://svcs.sandbox.paypal.com/AdaptivePayments/Pay'
    headers = {
    "X-PAYPAL-SECURITY-USERID": settings.PAYPAL_API_USER,
    "X-PAYPAL-SECURITY-PASSWORD": settings.PAYPAL_API_KEY,
    "X-PAYPAL-SECURITY-SIGNATURE": settings.PAYPAL_API_SIG,
    "X-PAYPAL-DEVICE-IPADDRESS": "117.192.38.155",
    "X-PAYPAL-REQUEST-DATA-FORMAT": "JSON",
    "X-PAYPAL-RESPONSE-DATA-FORMAT": "JSON",
    "X-PAYPAL-APPLICATION-ID":"APP-80W284485P519543T"
    }
    data = {"returnUrl":returnUrl, \
            "requestEnvelope":{"errorLanguage":"en_US"},"currencyCode":"USD", \
            "receiverList":{"receiver":receiverList},
            "cancelUrl":cancelUrl,\
            "actionType":"PAY"
    }
    data.update(**kwargs)
    import urllib, urllib2, json
    request = urllib2.Request(API_END_POINT, data = json.dumps(data), headers = headers)
    resp = json.loads(urllib2.urlopen(request).read())
    key = resp["payKey"]
    API_ENDPOINT = ""
    if settings.DEBUG:
        API_ENDPOINT = "https://www.sandbox.paypal.com/webscr"
    else:
        API_ENDPOINT = "https://www.paypal.com/webscr"
    return "%s?cmd=_ap-payment&paykey=%s"%(API_ENDPOINT,key)
    
    