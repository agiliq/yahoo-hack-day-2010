from django.db import models

from flickrimporter.models import FlickrPhoto

class Payment(models.Model):
    photo = models.ForeignKey(FlickrPhoto)
    paypal_txn_key = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s %s' % (self.photo.title, self.paypal_txn_key)