from django.contrib import admin
from data.models import Entry, Tag
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
	list_display = ('name',)
	ordering = ('name',)
	
	inlines = [
        EntryInline,
    ]