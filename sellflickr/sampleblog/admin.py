from django.contrib.admin import ModelAdmin, site
from sampleblog.models import Entry, make_author_abcd

class EntryAdmin(ModelAdmin):
    list_display = ('pub_date', 'headline', 'author', 'test_method')
    actions= [make_author_abcd,]
site.register(Entry, EntryAdmin)
