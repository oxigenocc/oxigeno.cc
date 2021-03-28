from django.urls import path, include
from distribuidores.api.v3 import urls as OxigenoUrls
from equipos.api.v3 import urls as EquiposUrls


urlpatterns = [
    path('', include(OxigenoUrls)),
    path('', include(EquiposUrls))
]