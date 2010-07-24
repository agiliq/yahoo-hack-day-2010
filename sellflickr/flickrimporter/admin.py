from subdomain_admin.admin import SubdomainAdmin
from django.contrib import admin
from flickrimporter.models import FlickrPhoto, FlickrUser

class FlickrPhotoAdmin(SubdomainAdmin):
    list_filter = ('customer','datetime')
    list_display = ('customer','datetime','get_thumbnail')
    search_fields = ['title',]


admin.site.register(FlickrPhoto)
admin.site.register(FlickrUser)
