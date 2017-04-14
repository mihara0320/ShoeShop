from django.conf.urls import url, include
from django.views.generic import View, ListView, DetailView
from . import views

urlpatterns = [
    url(r'^$', views.content_view, name = 'content'),
]
