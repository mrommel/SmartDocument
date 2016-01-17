from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import RequestContext, loader

from forecast.models import Category, Payment

# Create your views here.
def index(request):	
	categories = Category.objects.all()
	payments = Payment.objects.all()
	
	amount_per_year = 0
	
	for category in categories:
		amount_per_year = amount_per_year + category.amount()

	return render(request, 'forecast/index.html', { 'categories': categories, 'payments': payments, 'amount_per_year': amount_per_year })
