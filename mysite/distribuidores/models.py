from django.db import models
from django_google_maps import fields as map_fields
from simple_history.models import HistoricalRecords


# Create your models here.

class Estado(models.Model):
    nombre = models.CharField(max_length=30)
    alias = models.CharField(max_length=30)
    header = models.ImageField(upload_to='photos')
    footer = models.ImageField(upload_to='photos')

    class Meta:
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.nombre


class DistribuidorBaseModel(models.Model):
    estado_procedencia = models.ForeignKey(Estado, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    notas_internas = models.TextField(null=True, blank=True)
    notas = models.TextField(null=True, blank=True)
    direccion = models.TextField()
    link_pagina = models.CharField(max_length=100, null=True, blank=True)
    whatsapp = models.CharField(max_length=20, null=True, blank=True)
    a_domicilio = models.BooleanField()
    pago_con_tarjeta = models.BooleanField()
    horario = models.CharField(max_length=100, default='')
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True


class DistribuidorPotencial(DistribuidorBaseModel):
    rfc = models.CharField(max_length=13)
    ofrece_venta_de_tanque = models.BooleanField()
    ofrece_renta_de_tanque = models.BooleanField()
    ofrece_recarga_de_tanque = models.BooleanField()
    ofrece_venta_de_concentrador = models.BooleanField()
    ofrece_renta_de_concentrador = models.BooleanField()

    class Meta:
        verbose_name_plural = "distribuidores potenciales"
        db_table = 'distribuidor_potencial'

    def __str__(self):
        return self.nombre


class Distribuidor(DistribuidorBaseModel):
    estado = models.CharField(max_length=50)
    direccion = models.TextField()
    ciudad = models.CharField(max_length=100)
    address = map_fields.AddressField(max_length=200, default='')
    geolocation = map_fields.GeoLocationField(max_length=100, default='')
    dar_de_baja = models.BooleanField(default=False)
    abre_sabado = models.BooleanField(default=True)
    abre_domingo = models.BooleanField(default=True)
    abre_24h = models.BooleanField(default=True)
    recarga_gratis = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "distribuidores"
        db_table = 'distribuidor'

    def __str__(self):
        return self.nombre

