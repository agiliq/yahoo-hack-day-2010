from subdomain_admin.admin import SubdomainAdmin
from django.contrib import admin
from flickrimporter.models import FlickrPhoto, FlickrUser

admin.site.register(FlickrPhoto)
admin.site.register(FlickrUser)
