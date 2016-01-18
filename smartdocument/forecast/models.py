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