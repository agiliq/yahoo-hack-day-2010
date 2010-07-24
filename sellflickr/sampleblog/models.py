from django.db import models
from django.utils.html import mark_safe

class Entry(models.Model):
    pub_date = models.DateTimeField()
    author = models.CharField(max_length=32, help_text='Use the full name, e.g., "John Lennon".')
    slug = models.CharField(max_length=32)
    headline = models.CharField(max_length=255)
    summary = models.TextField(help_text='Use plain text (no HTML).')
    body = models.TextField(help_text='Use raw HTML, including &lt;p&gt; tags.')

    class Meta:
        verbose_name_plural = 'entries'

    def __unicode__(self):
        return self.headline

    def url(self):
        return "/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)

    def test_method(self):
        return mark_safe('<img src="http://eventbrite-s3.s3.amazonaws.com/eventlogos/1934679/ohindia2010logoforweb.jpg"/>')
    test_method.allow_tags = True
    

def make_author_abcd(modeladmin, request, queryset):
    queryset.update(author='abcd')
    make_author_abcd.short_description='Sets the price of all selected'
