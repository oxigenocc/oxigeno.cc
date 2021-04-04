from django.contrib import admin
from django.urls import path, include
from api.v2 import urls as APIV1Urlsv2
from api.v3 import urls as APIV1Urlsv3
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oxigeno/', include('oxigeno.urls')),
    path('manager/', include('manager.urls')),
    path('api/v2/', include(APIV1Urlsv2)),
    path('api/v3/', include(APIV1Urlsv3)),
    path('login/',TemplateView.as_view(
                                       template_name='index.html'), 
                                       name='login'
    ),
    path('distribuidores/',TemplateView.as_view(
                                       template_name='index.html'), 
                                       name='distribuidores'
    ),
    path('',TemplateView.as_view(
                                       template_name='index.html'), 
                                       name='index'
    ),
]
