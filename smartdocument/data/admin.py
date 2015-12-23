from django.contrib import admin

from data.models import Document, Tag, Entry
from data.forms import TagForm, EntryForm

admin.site.register(Entry, EntryForm)
admin.site.register(Document)
admin.site.register(Tag, TagForm)
