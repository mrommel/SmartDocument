from django.contrib import admin

from data.models import Document, Tag, Entry
from data.forms import TagForm

admin.site.register(Entry)
admin.site.register(Document)
admin.site.register(Tag, TagForm)
