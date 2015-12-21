from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    # tags
    url(r'^tags$', views.tags, name='data.views.tags'),
    url(r'^tag/(?P<tag_id>\d+)$', views.tag, name='data.views.tag'),
    # documents
    url(r'^documents$', views.documents, name='data.views.documents'),
    url(r'^document/(?P<document_id>\d+)$', views.document, name='data.views.document'),
]