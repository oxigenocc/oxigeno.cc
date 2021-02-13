from django.contrib import admin
from django.urls import path, include
from api.v2 import urls as APIV1Urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oxigeno/', include('oxigeno.urls')),
    path('manager/', include('manager.urls')),
    path('api/v2/', include(APIV1Urls))
]
