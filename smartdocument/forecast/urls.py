from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    # charts
    url(r'^charts$', views.charts, name='forecast.views.charts'),
    # timeline
    url(r'^timeline$', views.timeline, name='forecast.views.timeline'),
]