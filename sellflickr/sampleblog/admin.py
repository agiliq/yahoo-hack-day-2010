from django.contrib.admin import ModelAdmin, site
from sampleblog.models import Entry

class EntryAdmin(ModelAdmin):
    list_display = ('pub_date', 'headline', 'author')

site.register(Entry, EntryAdmin)
