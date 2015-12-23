from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import RequestContext, loader

from data.models import Tag, Document, Entry

from collections import OrderedDict

import logging

logger = logging.getLogger(__name__)

def index(request):
	tag_list = Tag.objects.all()
	category = {'U': 0, 'O': 0, 'N': 0, 'P': 0 }
	entries_list = Entry.objects.all()
	
	for entry in entries_list:
		category[entry.status] = category[entry.status] + entry.amount
	
	return render(request, 'data/index.html', {'tag_list': tag_list, 'category': category})
   
"""
	tag
""" 
def tags(request):
	tag_list = Tag.objects.all()

	return render(request, 'data/tags.html', {'tag_list': tag_list})
	
def tag(request, tag_id):
	tag = get_object_or_404(Tag, pk=tag_id)

	return render(request, 'data/tag.html', {'tag': tag})

"""
	document
"""
def documents(request):
	document_list = Document.objects.all()

	return render(request, 'data/documents.html', {'document_list': document_list})
	
def document(request, document_id):
	document = get_object_or_404(Document, pk=document_id)

	return render(request, 'data/document.html', {'document': document})
	
"""
	entry
"""
def entries(request):
	entries_list = Entry.objects.all()

	return render(request, 'data/entries.html', {'entries_list': entries_list})
	
def entry(request, entry_id):
	entry = get_object_or_404(Entry, pk=entry_id)

	return render(request, 'data/entry.html', {'entry': entry})
	
"""
	tables
"""
def tables(request):
	document_list = Document.objects.filter(type = 'T')
	
	months = OrderedDict()
	months['2014-10'] = 0
	months['2014-11'] = 0 
	months['2014-12'] = 0
	months['2015-01'] = 0
	months['2015-02'] = 0
	months['2015-03'] = 0
	months['2015-04'] = 0
	months['2015-05'] = 0
	months['2015-06'] = 0
	months['2015-07'] = 0
	months['2015-08'] = 0
	months['2015-09'] = 0
	months['2015-10'] = 0
	months['2015-11'] = 0
	months['2015-12'] = 0
	months['2016-01'] = 0
		
	for document in document_list:
		temp = str(document.date)[:7]
		for month in months.keys():
			if month == temp:
				months[month] = months[month] + document.entry.amount
				#logger.error('months[%s] = %s' % (month, months[month]))
				
		#logger.error('document %s - %s' % (temp, document.entry.amount))	

	return render(request, 'data/tables.html', {'stats': months })
	