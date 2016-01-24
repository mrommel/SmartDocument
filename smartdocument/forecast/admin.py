from django.contrib import admin

# Register your models here.
from forecast.models import Category, Payment, TimelineEntry, Gallery, Image
from forecast.forms import GalleryForm, TimelineEntryForm

admin.site.register(Category)
admin.site.register(Payment)
admin.site.register(TimelineEntry, TimelineEntryForm)
admin.site.register(Gallery, GalleryForm)
admin.site.register(Image)