from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    """ 
    	Allow entries to be categorised. 
    """
    name = models.CharField(max_length=40)
    
    def payments(self):
    	return Payment.objects.filter(category = self)
    
    def amount(self):
    	amount = 0
    	
    	for payment in self.payments():
    		amount = amount + payment.amount_per_year()
    	
    	return amount
    
    #@models.permalink
    #def get_absolute_url(self):
    #    return ('data.views.tag', [str(self.id)])
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ('name',)
        
class Payment(models.Model):
    """ 
    	Entry for planning 
    """
    name					= models.CharField(max_length=40)
    category 				= models.ForeignKey(Category)
    
    period 					= models.CharField(max_length=1, default="O", choices=(('O', 'Once'), ('M', 'Monthly'), ('Q', 'Quarterly'), ('Y', 'Yearly')))
    first_execution   		= models.DateField(null=True, blank=True)
    
    amount 					= models.DecimalField(max_digits=8, decimal_places=2)
    
    date_added   	= models.DateTimeField("added", auto_now_add=True)
    date_updated 	= models.DateTimeField("updated", auto_now=True) 
    
    def amount_per_year(self):
    	if self.period == 'M':
    		return self.amount * 12
    		
    	if self.period == 'Q':
    		return self.amount * 4
    		
    	if self.period == 'Y':
    		return self.amount
    		
    	return self.amount
    
    def __unicode__(self):
        return self.name or u"untitled"
        
class Gallery(models.Model):
    """ 
    	Entry for gallery 
    """
    title					= models.CharField(max_length=40)
    description				= models.CharField(max_length=500)
    
    date_added   			= models.DateTimeField("added", auto_now_add=True)
    date_updated 			= models.DateTimeField("updated", auto_now=True) 
    
    def images(self):
    	return Image.objects.filter(gallery = self)
    
    def __unicode__(self):
        return self.title or u"untitled"
        
class Image(models.Model):
    """ 
    	Entry for image 
    """
    title					= models.CharField(max_length=40)
    description				= models.CharField(max_length=500)
    
    gallery 				= models.ForeignKey(Gallery, blank=True, null=True)
    image 					= models.ImageField(upload_to='media/gallery', blank=True, null=True)
    
    date_added   			= models.DateTimeField("added", auto_now_add=True)
    date_updated 			= models.DateTimeField("updated", auto_now=True) 
    
    def thumbnail(self):
        if self.image.name is not None and self.image.name <> '':
            return '<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>' % ((self.image.name, self.image.name))
        else:
            return '<img border="0" alt="" src="/static/data/images/Person-icon-grey.JPG" height="40" />'
    thumbnail.allow_tags = True
    
    def __unicode__(self):
        return self.title or u"untitled"
        
class TimelineEntry(models.Model):
    """ 
    	Entry for timeline 
    """
    title					= models.CharField(max_length=40)
    description				= models.CharField(max_length=500)
    event_type 				= models.CharField(max_length=1, default="T", choices=(('T', 'Text'), ('P', 'Picture'), ('G', 'Gallery')))
    date   					= models.DateField(null=True, blank=True)
    
    image 					= models.ImageField(upload_to='media/timeline', blank=True, null=True)  
    gallery 				= models.ForeignKey(Gallery, blank=True, null=True)
    
    date_added   			= models.DateTimeField("added", auto_now_add=True)
    date_updated 			= models.DateTimeField("updated", auto_now=True) 
    
    def __unicode__(self):
        return self.title or u"untitled"
    