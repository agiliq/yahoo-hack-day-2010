from subdomain_admin.admin import SubdomainAdmin
from django.contrib import admin
from flickrimporter.models import FlickrPhoto, FlickrUser

class FlickrPhotoAdmin(SubdomainAdmin):
    list_filter = ('price',)
    list_editable = ('price',)
    list_display = ('get_thumbnail','title')
    search_fields = ['title',]


admin.site.register(FlickrPhoto,FlickrPhotoAdmin)
admin.site.register(FlickrUser)
