# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FlickrUser(models.Model):
    user = models.ForeignKey(User)
    token = models.CharField(max_length=100, unique=True)

class FlickrPhoto(models.Model):
    flickr_id = models.CharField(max_length=15)
    owner = models.ForeignKey(FlickrUser)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    server = models.IntegerField()
    secret = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    farm = models.IntegerField()
    
    class Admin:
        list_display = ('title',)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return "/photos/%s/" % (self.id)

    def get_image_url(self, size='small'):
        # small_square=75x75
        # thumb=100 on longest side
        # small=240 on longest side
        # medium=500 on longest side
        # large=1024 on longest side
        # original=duh
    
        base_url = "http://static.flickr.com"
        size_char='s'  # default to small_square
        
        if size == 'small_square':
            size_char='_s'
        elif size == 'thumb':
            size_char='_t'
        elif size == 'small':
            size_char='_m'
        elif size == 'medium':
            size_char=''
        elif size == 'large':
            size_char='_b'
        elif size == 'original':
            size_char='_o'
        
        return "%s/%s/%s_%s%s.jpg" % (base_url, 
                                      self.server, 
                                      self.flickr_id, 
                                      self.secret, 
                                      size_char)
    
    def get_thumbnail(self):
        return self.get_image_url(size=thumb)