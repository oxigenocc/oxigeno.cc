from django.urls import path, include
from rest_framework.routers import DefaultRouter
from oxigeno.api.v2.views import DistribuidorListViewSet,\
    ManagerDistribuidorUpdateViewSet

distribuidor_router = DefaultRouter()
distribuidor_router.register(r'', DistribuidorListViewSet)

manager_router = DefaultRouter()
manager_router.register(r'distribuidor', ManagerDistribuidorUpdateViewSet)


urlpatterns = [
    path('data/', include(distribuidor_router.urls)),
    path('manager/', include(manager_router.urls)),
]