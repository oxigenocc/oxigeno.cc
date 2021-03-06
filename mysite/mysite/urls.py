from django.contrib import admin
from django.urls import path, include
from api.v2 import urls as APIV1Urls
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oxigeno/', include('oxigeno.urls')),
    path('manager/', include('manager.urls')),
    path('api/v2/', include(APIV1Urls)),
    path('login/',TemplateView.as_view(
                                       template_name='index.html'), 
                                       name='login'
    ),
]
