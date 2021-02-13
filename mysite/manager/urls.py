from django.urls import path

from django.views.generic import TemplateView

from . import views_v1_2

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='manager'),
    path('v1.2/distribuidor', views_v1_2.rest_post, name='rest_post_v1_2'),
    path('v1.2/login', views_v1_2.manager_login, name='manager_login_v1_2'),
    path('v1.2/logout', views_v1_2.manager_logout, name='manager_logout_v1_2'),
]