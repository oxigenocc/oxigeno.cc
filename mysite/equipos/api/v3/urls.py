from django.urls import path, include
from rest_framework.routers import DefaultRouter
from oxigeno.api.v2.views import TanqueHistoricalViewSet,\
    ConcentradorHistoricalViewSet

distribuidor_router = DefaultRouter()
distribuidor_router.register(r'tanque/historical',
                             TanqueHistoricalViewSet)
distribuidor_router.register(r'concentrador/historical',
                             ConcentradorHistoricalViewSet)

urlpatterns = [
    path('<int:estado>/equipos/', include(distribuidor_router.urls)),
]