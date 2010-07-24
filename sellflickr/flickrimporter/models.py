from django.db import models

# Create your models here.

class FlickrUser(models.Model):
    user = models.ForeignKey(User, related_name='flickr_profiles')

class FlickrPhoto(modes.Model):
    owner = models.ForeignKey(FlickrUser)
    
    def get_image_url(self, size):
        return ""