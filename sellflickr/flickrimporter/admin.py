from subdomain_admin.admin import SubdomainAdmin
from django.contrib import admin
from flickrimporter.models import FlickrPhoto, FlickrUser

class FlickrPhotoAdmin(SubdomainAdmin):
    list_filter = ('price',)
    list_editable = ('price',)
    list_display = ('show_thumbnail','title','price')
    search_fields = ['title',]


admin.site.register(FlickrPhoto,FlickrPhotoAdmin)
admin.site.register(FlickrUser)
