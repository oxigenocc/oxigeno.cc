import pytz
from datetime import datetime
from rest_framework import serializers
from oxigeno.models import Distribuidor, Concentrador, Tanque


class TanqueSerializer(serializers.ModelSerializer):
    renta = serializers.SerializerMethodField()
    venta = serializers.SerializerMethodField()
    recarga = serializers.SerializerMethodField()

    class Meta:
        model = Tanque
        fields = ('renta', 'disponibilidad_renta', 'venta',
                  'disponibilidad_venta', 'recarga', 'disponibilidad_recarga')


    def get_renta(self, obj):
        return obj.ofrece_renta

    def get_venta(self, obj):
        return obj.ofrece_recarga

    def get_recarga(self, obj):
        return obj.ofrece_recarga


class ConcentradorSerializer(serializers.ModelSerializer):
    renta = serializers.SerializerMethodField()
    venta = serializers.SerializerMethodField()

    class Meta:
        model = Concentrador
        fields = ('renta', 'disponibilidad_renta', 'venta',
                  'disponibilidad_venta')

    def get_renta(self, obj):
        return obj.ofrece_renta

    def get_venta(self, obj):
        return obj.ofrece_venta


class DistribuidorSerializer(serializers.ModelSerializer):
    concentradores = serializers.SerializerMethodField()
    tanques = serializers.SerializerMethodField()
    lat = serializers.SerializerMethodField()
    lng = serializers.SerializerMethodField()

    class Meta:
        model = Distribuidor
        fields = ('concentradores', 'tanques', 'id', 'horario', 'estado',
                  'direccion', 'ciudad', 'a_domicilio', 'pago_con_tarjeta',
                  'notas', 'telefono', 'ultima_actualizacion', 'lat', 'lng',
                  'whatsapp', 'link_pagina')

    def get_concentradores(self, obj):
        concentradores = obj.concentrador_set.all()
        return ConcentradorSerializer(instance=concentradores,
                                      many=True).data

    def get_tanques(self, obj):
        tanques = obj.tanque_set.all()
        return TanqueSerializer(instance=tanques, many=True).data

    def get_location(self, geo, position):
        return str(geo).split(',')[position]

    def get_lat(self, obj):
        return self.get_location(obj.geolocation, 0)

    def get_lng(self, obj):
        return self.get_location(obj.geolocation, 1)

    def get_ultima_actualizacion(self, obj):
        max_tanque = max(
            tanque.ultima_actualizacion for tanque in obj.tanque_set.all()) \
            if obj.tanque_set.all() else datetime.min.replace(tzinfo=pytz.UTC)
        max_concentrador = max(
            concentrador.ultima_actualizacion for concentrador in
            obj.concentrador_set.all()) if obj.concentrador_set.all() \
            else datetime.min.replace(tzinfo=pytz.UTC)
        ultima_actualización = max(
            [obj.ultima_actualizacion, max_tanque, max_concentrador])
        return str(ultima_actualización)