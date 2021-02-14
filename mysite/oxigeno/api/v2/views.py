from django.db.models.functions import Greatest, Coalesce
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from oxigeno.models import Distribuidor, Tanque, Concentrador,\
    DistribuidorPotencial
from oxigeno.api.v2.serializers import DistribuidorSerializer,\
    DistribuidorUpdateSerializer, DistribuidorPotencialSerializer
from oxigeno.api.v2.filters import DistribuidorFilterSet


class DistribuidorListViewSet(mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    queryset = Distribuidor.objects.all()
    serializer_class = DistribuidorSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = DistribuidorFilterSet

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().annotate(
            max_value=Greatest(
                         'tanque__disponibilidad_renta',
                         'tanque__disponibilidad_venta',
                         'tanque__disponibilidad_recarga',
                         'concentrador__disponibilidad_venta',
                         'concentrador__disponibilidad_renta'
                         , 0)).order_by('-max_value'))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=200)



class ManagerDistribuidorUpdateViewSet(mixins.CreateModelMixin,
                                       viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Distribuidor.objects.all()
    serializer_class = DistribuidorUpdateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            distribuidor = serializer.distribuidor
            tanque = Tanque.objects.filter(
                id=distribuidor[0].tanque_set.all()[0].id)
            concentrador = Concentrador.objects.filter(
                id=distribuidor[0].concentrador_set.all()[0].id)
            tanque.update(**serializer.tanque_data)
            concentrador.update(**serializer.concentrador_data)
            distribuidor.update(**serializer.distribuidor_data)
        except Exception as e:
            return Response(data=str(e), status=400)
        return Response(status=200)


class DistribuidorPotencialCreateViewSet(mixins.CreateModelMixin,
                                         viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    queryset = DistribuidorPotencial.objects.all()
    serializer_class = DistribuidorPotencialSerializer

