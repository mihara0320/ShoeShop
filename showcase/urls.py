from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from showcase.models import Item
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^new_arrival/$', views.new_arrivals_view, name = 'new_arrival'),
    url(r'^brand_list/$', views.brand_list_view, name = 'brand_list'),
    url(r'^(?P<pk>\d+)$', views.ItempageView.as_view(), name = 'itempage'),

]
