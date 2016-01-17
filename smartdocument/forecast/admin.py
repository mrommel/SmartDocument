from django.contrib import admin

# Register your models here.
from forecast.models import Category, Payment
#from forecast.forms import CategoryForm

admin.site.register(Category)
admin.site.register(Payment)