from django.db import models
from django_google_maps import fields as map_fields
from simple_history.models import HistoricalRecords


# Create your models here.


class Distribuidor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_distribuidor = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    direccion = models.TextField()    
    ciudad = models.CharField(max_length=100)
    a_domicilio =  models.BooleanField()
    pago_con_tarjeta = models.BooleanField()
    notas = models.TextField(null=True, blank=True)
    telefono = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20, null=True, blank= True)
    link_pagina = models.CharField(max_length=100, null=True, blank=True)        
    address = map_fields.AddressField(max_length=200, default='')
    geolocation = map_fields.GeoLocationField(max_length=100, default='')
    # dar_de_baja = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta: 
        verbose_name_plural = "distribuidores"


    def __str__(self):
        return self.nombre_distribuidor

class Tanque(models.Model):
    id = models.AutoField(primary_key=True)
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.CASCADE)

    # ofrece_renta = models.BooleanField(default=True)
    disponibilidad_renta = models.IntegerField()
    # ofrece_venta = models.BooleanField(default=True)
    disponibilidad_venta = models.IntegerField()
    # ofrece_recarga = models.BooleanField(default=True)
    disponibilidad_recarga = models.IntegerField()

    ultima_actualizacion = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()


    def __str__(self):
        return "Tanque - " + self.distribuidor.nombre_distribuidor

class Concentrador(models.Model):
    id = models.AutoField(primary_key=True)
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.CASCADE)

    # ofrece_renta = models.BooleanField(default=True)
    disponibilidad_renta = models.IntegerField()
    # ofrece_venta = models.BooleanField(default=True)
    disponibilidad_venta = models.IntegerField()

    ultima_actualizacion = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()


    def __str__(self):
        return "Concentrador - " + self.distribuidor.nombre_distribuidor

    
    class Meta: 
        verbose_name_plural = "concentradores"
