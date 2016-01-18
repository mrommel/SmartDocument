from django.contrib import admin

from data.models import Document, Tag, Entry, Action
from data.forms import TagForm, EntryForm, DocumentForm

admin.site.register(Entry, EntryForm)
admin.site.register(Document, DocumentForm)
admin.site.register(Tag, TagForm)
admin.site.register(Action)