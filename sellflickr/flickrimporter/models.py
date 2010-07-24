# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FlickrUser(models.Model):
    user = models.ForeignKey(User)

class FlickrPhoto(models.Model):
    owner = models.ForeignKey(FlickrUser)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def get_image_url(self, size):
        return ""