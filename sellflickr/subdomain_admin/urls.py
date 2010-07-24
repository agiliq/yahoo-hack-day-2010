from django.conf.urls.defaults import *

urlpatterns = patterns('subdomain_admin.views',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    url(r'^new/', 'create_subdomain' , name='create_subdomain'),
)