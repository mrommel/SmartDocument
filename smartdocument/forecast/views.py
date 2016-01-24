from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import RequestContext, loader

from forecast.models import Category, Payment, TimelineEntry

from collections import OrderedDict

from operator import attrgetter

# Create your views here.
def index(request):	
	categories = Category.objects.all()
	payments = Payment.objects.all()
	
	amount_per_year = 0
	
	for category in categories:
		amount_per_year = amount_per_year + category.amount()

	return render(request, 'forecast/index.html', { 'categories': categories, 'payments': payments, 'amount_per_year': amount_per_year })

# timeline
def timeline(request):	

	timelineEntries = TimelineEntry.objects.all()
	
	sorted_timeline = sorted(timelineEntries, key=attrgetter('date'), reverse=True)

	return render(request, 'forecast/timeline.html', { 'timelineEntries': sorted_timeline })


def charts(request):
	payments = Payment.objects.all()
	
	months = OrderedDict()
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
		
	for payment in payments:
		temp = str(payment.first_execution)[:7]
		
		for month in months.keys():
			if payment.period == 'O':
				if month == temp:
					months[month] = months[month] + payment.amount
				#logger.error('months[%s] = %s' % (month, months[month]))
				
			if payment.period == 'M':
				#return self.amount * 12
				pass
			
			if payment.period == 'Q':
				#return self.amount * 4
				pass
			
			if payment.period == 'Y':
				#return self.amount
				pass
				
		#logger.error('document %s - %s' % (temp, document.entry.amount))	

	return render(request, 'forecast/charts.html', {'stats': months })