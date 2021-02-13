from django.urls import path, include
from oxigeno.api.v2 import urls as OxigenoUrls
from users.api.v2 import urls as UserUrls


urlpatterns = [
    path('', include(OxigenoUrls)),
    path('', include(UserUrls))
]