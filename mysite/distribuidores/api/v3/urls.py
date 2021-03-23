from django.urls import path, include
from rest_framework.routers import DefaultRouter
from distribuidores.api.v3.views import EstadoListViewSet,\
    DistribuidorListViewSet, DistribuidorPotencialHistoricalViewSet,\
    DistribuidorHistoricalViewSet, ManagerDistribuidorUpdateViewSet,\
    DistribuidorPotencialCreateViewSet

estado_router = DefaultRouter()
estado_router.register(r'estados', EstadoListViewSet)

distribuidor_router = DefaultRouter()
distribuidor_router.register(r'', DistribuidorListViewSet)
distribuidor_router.register(r'distribuidor-potencial/historical',
                             DistribuidorPotencialHistoricalViewSet)
distribuidor_router.register(r'distribuidor/historical',
                             DistribuidorHistoricalViewSet)


manager_router = DefaultRouter()
manager_router.register(r'distribuidor', ManagerDistribuidorUpdateViewSet)

potencial_router = DefaultRouter()
potencial_router.register(r'formulario', DistribuidorPotencialCreateViewSet)


urlpatterns = [
    path('', include(estado_router.urls)),
    path('<int:estado>/data/', include(distribuidor_router.urls)),
    path('<int:estado>/manager/', include(manager_router.urls)),
    path('<int:estado>/potencial/', include(potencial_router.urls))
]