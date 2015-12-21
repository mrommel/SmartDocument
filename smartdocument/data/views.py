from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import RequestContext, loader

from data.models import Tag, Document

def index(request):
	tag_list = Tag.objects.all()
	
	return render(request, 'data/index.html', {'tag_list': tag_list})
   
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