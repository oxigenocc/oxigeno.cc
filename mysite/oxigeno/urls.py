from django.urls import path

from django.views.generic import TemplateView

from . import views
from . import views_v1_1

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('data', views.rest_get, name='rest_get'),
    path('v1.1/data', views_v1_1.rest_get, name='rest_get_v1_1'),
    path('v1.1/data/<int:id_distribuidor>', views_v1_1.rest_get_single, name='rest_get_single_v1_1'),
]