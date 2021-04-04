from django.urls import path

from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('formulario/', TemplateView.as_view(template_name='index.html'), name='formulario'),
]