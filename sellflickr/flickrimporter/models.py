# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from subdomains.models import Subdomain
# Create your models here.

class FlickrUser(models.Model):
    nsid = models.CharField(max_length=15)
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
    subdomain = models.ForeignKey(Subdomain)
    
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
    
        base_url = "http://farm%s.static.flickr.com"
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
        
        return "%s/%s/%s_%s%s.jpg" % (base_url % (self.farm), 
                                      self.server, 
                                      self.flickr_id, 
                                      self.secret, 
                                      size_char)
    
    @property
    def thumbnail_image(self):
        return self.get_image_url(size='thumb')
    
    @property
    def small_image(self):
        return self.get_image_url('small')
    
    @property
    def medium_image(self):
        return self.get_image_url('medium')
    
    @property
    def large_image(self):
        return self.get_image_url('large')
    
    @property
    def orig_image(self):
        return self.get_image_url('original')
    
    @property
    def get_price(self):
        return self.price or 10
    
    def show_thumbnail(self):
        return '<img src="%s" />'%self.thumbnail_image()