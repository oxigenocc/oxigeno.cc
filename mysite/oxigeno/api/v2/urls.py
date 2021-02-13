from django.urls import path, include
from rest_framework.routers import DefaultRouter
from oxigeno.api.v2.views import DistribuidorListViewSet

router = DefaultRouter()
router.register(r'', DistribuidorListViewSet)


urlpatterns = [
    path('data/', include(router.urls)),
]