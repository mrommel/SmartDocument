from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import RequestContext, loader

from data.models import Tag, Document, Entry, Action

from collections import OrderedDict

import logging

logger = logging.getLogger(__name__)

def index(request):
	tag_list = Tag.objects.all()
	category = {u'Unsure': 0, u'Open': 0, u'Ordered': 0, u'Payed': 0 }
	creditable_entries = {u'Unsure': [], u'Yes': [], u'No': [], u'Ignore': [] }
	creditable_sum = {u'Unsure': 0, u'Yes': 0, u'No': 0, u'Ignore': 0 }
	entries_list = Entry.objects.filter()
	
	next_entries_list = []
	
	for entry in entries_list:
		category[entry.get_status_display()] = category[entry.get_status_display()] + entry.amount
		
		if entry.status == 'N':
			next_entries_list.append(entry)
			
		creditable_entries[entry.get_creditable_display()].append(entry)
		
		creditable_sum[entry.get_creditable_display()] = creditable_sum[entry.get_creditable_display()] + entry.amount
			
	actions = Action.objects.filter()
	
	return render(request, 'data/index.html', {'tag_list': tag_list, 'category': category, 'next_entries_list': next_entries_list, 'actions': actions, 'creditable': creditable_entries, 'creditable_sum': creditable_sum })
   
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
	charts
"""
def charts(request):
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
	months['2016-02'] = 0
	months['2016-03'] = 0
	months['2016-04'] = 0
	months['2016-05'] = 0
	months['2016-06'] = 0
	months['2016-07'] = 0
	months['2016-08'] = 0
	months['2016-09'] = 0
	months['2016-10'] = 0
	months['2016-11'] = 0
	months['2016-12'] = 0
		
	for document in document_list:
		temp = str(document.date)[:7]
		for month in months.keys():
			if month == temp:
				months[month] = months[month] + document.entry.amount
				#logger.error('months[%s] = %s' % (month, months[month]))
				
		#logger.error('document %s - %s' % (temp, document.entry.amount))	

	return render(request, 'data/charts.html', {'stats': months })
	
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
	months['2016-02'] = 0
	months['2016-03'] = 0
	months['2016-04'] = 0
	months['2016-05'] = 0
	months['2016-06'] = 0
	months['2016-07'] = 0
	months['2016-08'] = 0
	months['2016-09'] = 0
	months['2016-10'] = 0
	months['2016-11'] = 0
	months['2016-12'] = 0
		
	for document in document_list:
		temp = str(document.date)[:7]
		for month in months.keys():
			if month == temp:
				months[month] = months[month] + document.entry.amount
				#logger.error('months[%s] = %s' % (month, months[month]))
				
		#logger.error('document %s - %s' % (temp, document.entry.amount))	

	return render(request, 'data/tables.html', {'stats': months })
	