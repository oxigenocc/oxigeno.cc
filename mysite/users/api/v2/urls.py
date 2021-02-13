from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserLoginViewSet

router = DefaultRouter()
router.register(r'login', UserLoginViewSet, basename='login')


urlpatterns = [
    path('manager/', include(router.urls)),
]