from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser
from equipos.models import Tanque, Concentrador
from equipos.api.v3.serializers import TanqueHistoricalSerializer,\
    ConcentradorHistoricalSerializer


class TanqueHistoricalViewSet(mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Tanque.objects.all()
    serializer_class = TanqueHistoricalSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(distribuidor__estado_procedencia__id=
                         self.kwargs['estado'])


class ConcentradorHistoricalViewSet(mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    permission_classes = (IsAdminUser,)
    queryset = Concentrador.objects.all()
    serializer_class = ConcentradorHistoricalSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(distribuidor__estado_procedencia__id=
                         self.kwargs['estado'])
