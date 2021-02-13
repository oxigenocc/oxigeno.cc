from django.urls import path, include
from oxigeno.api.v2 import urls as OxigenoUrls
urlpatterns = [
    path('', include(OxigenoUrls)),
]