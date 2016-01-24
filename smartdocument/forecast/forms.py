from django.contrib import admin
from forecast.models import Image, Gallery, TimelineEntry
from django.db import models
from django import forms

class ImageInline(admin.TabularInline):
	model = Image
	fk_name = "gallery"
	readonly_fields = ('thumbnail',)
	fields = ('title', 'thumbnail')

class GalleryForm(admin.ModelAdmin):
	model = Gallery
	list_display = ('title', 'number_of_images',)
	ordering = ('title',)
	
	inlines = [
		ImageInline,
	]
	
	def number_of_images(self, instance):
		images = 0
		
		for entry in instance.images():
			images = images + 1
		
		return images
		
class TimelineEntryForm(admin.ModelAdmin):
	model = TimelineEntry
	list_display = ('title', 'date', 'event_type',)
	ordering = ('title',)
	