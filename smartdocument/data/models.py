import os
import uuid

from django.db import models
	
from mimetypes import guess_type

def get_filename_from_uuid(instance, filename, directory='documents'):
    populate_file_extension_and_mimetype(instance, filename)
    stem, extension = os.path.splitext(filename)
    return '%s/%s%s' % (directory, instance.uuid, extension)

def populate_file_extension_and_mimetype(instance, filename):
    # First populate the file extension and mimetype
    instance.file_mimetype, encoding = guess_type(filename) or ""
    slug, instance.file_extension = os.path.splitext(filename)

class Tag(models.Model):
    """ 
    	Allow entries to be categorised. 
    """
    name = models.CharField(max_length=40)
    
    def entries(self):
    	return Entry.objects.filter(tag = self)
    
    def amount(self):
    	amount = 0
    	
    	for entry in self.entries():
    		amount = amount + entry.amount
    	
    	return amount
    
    @models.permalink
    def get_absolute_url(self):
        return ('data.views.tag', [str(self.id)])
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ('name',)

class Entry(models.Model):
    """ 
    	Entry for planning 
    """
    name					= models.CharField(max_length=40)
    tag 					= models.ForeignKey(Tag)
    
    status 					= models.CharField(max_length=1, default="U", choices=(('U', 'Unsure'), ('O', 'Ordered'), ('N', 'Open'), ('P', 'Payed')))
    
    amount 					= models.DecimalField(max_digits=8, decimal_places=2)
    
    def order(self):
    	return Document.objects.filter(entry = self, type = 'O')
    	
    def bill(self):
    	return Document.objects.filter(entry = self, type = 'B')
    	
    def transfer(self):
    	return Document.objects.filter(entry = self, type = 'T')
    
    @models.permalink
    def get_absolute_url(self):
        return ('data.views.entry', [str(self.id)])
    
    def __unicode__(self):
        return self.name or u"untitled"
    
    class Meta:
        ordering = ('name',)

class Document(models.Model):
    """ 
    	Basic document entry for larger document databases.
    """
    uuid           	= models.CharField(max_length=36, default=u'%s' % (uuid.uuid4()), blank=True, editable=False)
    title        	= models.CharField(max_length=150, default="", blank=True)
    summary      	= models.TextField(default="", blank=True)
    date   			= models.DateField(null=True, blank=True)
    
    type 			= models.CharField(max_length=1, default="O", choices=(('O', 'Order'), ('B', 'Bill'), ('T', 'Transfer')))
    
    entry 			= models.ForeignKey(Entry)
    
    file           	= models.FileField(upload_to=get_filename_from_uuid, null=True, blank=True)
    
    date_added   	= models.DateTimeField("added", auto_now_add=True)
    date_updated 	= models.DateTimeField("updated", auto_now=True) 
    
    def __unicode__(self):
        return self.title or u"untitled"
    