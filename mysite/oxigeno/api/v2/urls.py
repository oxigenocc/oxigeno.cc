from django.urls import path, include
from rest_framework.routers import DefaultRouter
from oxigeno.api.v2.views import DistribuidorListViewSet,\
    ManagerDistribuidorUpdateViewSet, DistribuidorPotencialCreateViewSet,\
    DistribuidorHistoricalViewSet, TanqueHistoricalViewSet,\
    ConcentradorHistoricalViewSet, DistribuidorPotencialHistoricalViewSet

distribuidor_router = DefaultRouter()
distribuidor_router.register(r'', DistribuidorListViewSet)
distribuidor_router.register(r'distribuidor/historical',
                             DistribuidorHistoricalViewSet)
distribuidor_router.register(r'tanque/historical',
                             TanqueHistoricalViewSet)
distribuidor_router.register(r'concentrador/historical',
                             ConcentradorHistoricalViewSet)
distribuidor_router.register(r'distribuidor-potencial/historical',
                             DistribuidorPotencialHistoricalViewSet)

manager_router = DefaultRouter()
manager_router.register(r'distribuidor', ManagerDistribuidorUpdateViewSet)

potencial_router = DefaultRouter()
potencial_router.register(r'formulario', DistribuidorPotencialCreateViewSet)


urlpatterns = [
    path('data/', include(distribuidor_router.urls)),
    path('manager/', include(manager_router.urls)),
    path('potencial/', include(potencial_router.urls))
]