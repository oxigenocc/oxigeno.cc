from django_filters.rest_framework import FilterSet
from django_filters.filters import NumberFilter, CharFilter
from oxigeno.models import Distribuidor


class DistribuidorFilterSet(FilterSet):
    tanqueVenta = NumberFilter(
        method='filter_field_gt',
        field_name='tanque__disponibilidad_venta')
    tanqueRecarga = NumberFilter(
        method='filter_field_gt',
        field_name='tanque__disponibilidad_recarga')
    tanqueRenta = NumberFilter(
        method='filter_field_gt',
        field_name='tanque__disponibilidad_renta')
    concentradorVenta = NumberFilter(
        method='filter_field_gt',
        field_name='concentrador__disponibilidad_venta')
    concentradorRenta = NumberFilter(
        method='filter_field_gt',
        field_name='concentrador__disponibilidad_renta')
    pagoConTarjeta = NumberFilter(
        method='filter_field_bool',
        field_name='pago_con_tarjeta')
    aDomicilio = NumberFilter(
        method='filter_field_bool',
        field_name='a_domicilio')
    incluirBajas = NumberFilter(
        method='filter_field_bool',
        field_name='dar_de_baja')
    abiertoFin = NumberFilter(
        method='filter_field_bool',
        field_name='abre_fin_de_semana')
    abierto24 = NumberFilter(
        method='filter_field_bool',
        field_name='abre_24h')
    gratis = NumberFilter(
        method='filter_field_bool',
        field_name='recarga_gratis')
    nombreComo = CharFilter(
        method='filter_char_containts',
        field_name='nombre_distribuidor__unaccent')

    def filter_field_gt(self, queryset, name, value):
        lookup = '__'.join([name, 'gt'])
        return queryset.filter(**{lookup: 0}).distinct()

    def filter_field_bool(self, queryset, name, value):
        return queryset.filter(**{name: bool(value)}).distinct()

    def filter_char_containts(self, queryset, name, value):
        lookup = '__'.join([name, 'icontains'])
        return queryset.filter(**{lookup: value}).distinct()

    class Meta:
        model = Distribuidor
        fields = ('tanqueVenta', 'tanqueRecarga', 'tanqueRenta',
                  'concentradorVenta', 'concentradorRenta', 'pagoConTarjeta',
                  'aDomicilio', 'incluirBajas', 'nombreComo', 'abiertoFin',
                  'abierto24', 'gratis')