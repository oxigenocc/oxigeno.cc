from django.urls import path

from django.views.generic import TemplateView

from . import views
from . import views_v1_1
from . import views_v1_2

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('data', views.rest_get, name='rest_get'),
    path('v1.1/data', views_v1_1.rest_get, name='rest_get_v1_1'),
    path('v1.1/data/<int:id_distribuidor>', views_v1_1.rest_get_single, name='rest_get_single_v1_1'),
    path('v1.2/data', views_v1_2.rest_get, name='rest_get_v1_2'),
    path('v1.2/data/<int:id_distribuidor>', views_v1_2.rest_get_single, name='rest_get_single_v1_2'),
    path('v1.2/data/<int:id_distribuidor>', views_v1_2.rest_get_single, name='rest_get_single_v1_2'),
    path('formulario/', TemplateView.as_view(template_name='index.html'), name='formulario'),
    path('formulario/data', views_v1_2.rest_post_distribuidor_potencial, name='rest_post_distribuidor_potencial_v1_2')
]