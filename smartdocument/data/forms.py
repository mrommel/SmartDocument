from django.contrib import admin
from data.models import Entry, Tag, Document
from django.db import models
from django import forms

class EntryInline(admin.TabularInline):
	model = Entry
	fk_name = "tag"
	readonly_fields = ('name',)
	fields = ('name', 'status', 'amount')
	
	def get_extra (self, request, obj=None, **kwargs):
		""" hide all extra """
		return 0

class TagForm(admin.ModelAdmin):
	model = Tag
	list_display = ('name', 'entries',)
	ordering = ('name',)
	
	inlines = [
		EntryInline,
	]
	
	def entries(self, instance):
		entries_str = ''
		
		for entry in instance.entries():
			entries_str = '%s, %s' % (entries_str, str(entry))
			
		entries_str = "$%s$" % (entries_str)
		entries_str = entries_str.replace("$, ", "")
		entries_str = entries_str.replace(", $", "")
		entries_str = entries_str.replace("$", "")
		
		return entries_str
    
class DocumentInline(admin.TabularInline):
	model = Document
	fk_name = "entry"
	readonly_fields = ('title',)
	fields = ('title', 'date', 'type')
	
	def get_extra (self, request, obj=None, **kwargs):
		""" hide all extra """
		return 0
    
class EntryForm(admin.ModelAdmin):
	model = Entry
	list_display = ('name', 'tag_name', 'amount', 'status',)
	ordering = ('name',)
	
	inlines = [
		DocumentInline,
	]
	
	def tag_name(self, instance):
		return str(instance.tag)
		