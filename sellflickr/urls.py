from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    (r'^flickr/', include('flickrimporter.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    url(r'', include('subdomain_admin.urls')),
    (r'', include('flickrpayments.urls')),
    url(r'home/', direct_to_template,{'template':'homepage.html'},name='homepage'),
)

#For static and media files
urlpatterns += patterns('',
                        (r'^admin_media/(.*)', 'django.views.static.serve',
                         {'document_root': 'admin_media',
                          'show_indexes':True}),
                        (r'^media/(.*)', 'django.views.static.serve',
                         {'document_root': 'media',
                          'show_indexes':True}),
                        )
