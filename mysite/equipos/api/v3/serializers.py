from rest_framework import serializers
from equipos.models import Tanque, Concentrador


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
        return obj.ofrece_venta

    def get_recarga(self, obj):
        return obj.ofrece_recarga


class TanqueHistoricalSerializer(serializers.ModelSerializer):
    history = serializers.SerializerMethodField()

    class Meta:
        model = Tanque
        fields = '__all__'

    def get_history(self, obj):
        model = obj.history.__dict__['model']
        fields = '__all__'
        from distribuidores.api.v3.serializers import \
            HistoricalRecordSerializer
        serializer = HistoricalRecordSerializer(model,
                              obj.history.all().order_by('history_id'),
                              fields=fields, many=True)
        serializer.is_valid()
        return serializer.data


class ConcentradorHistoricalSerializer(serializers.ModelSerializer):
    history = serializers.SerializerMethodField()

    class Meta:
        model = Concentrador
        fields = '__all__'

    def get_history(self, obj):
        model = obj.history.__dict__['model']
        fields = '__all__'
        from distribuidores.api.v3.serializers import \
            HistoricalRecordSerializer
        serializer = HistoricalRecordSerializer(model,
                                                obj.history.all().order_by(
                                                    'history_id'),
                                                fields=fields, many=True)
        serializer.is_valid()
        return serializer.data