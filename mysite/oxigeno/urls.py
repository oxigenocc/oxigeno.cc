from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data', views.rest_get, name='rest_get'),
]