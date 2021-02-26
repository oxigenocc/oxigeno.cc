from django.urls import path

from django.views.generic import TemplateView

from . import views_v1_2

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='manager'),
]