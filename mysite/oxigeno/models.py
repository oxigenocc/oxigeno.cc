from django.db import models

# Create your models here.


class Distribuidor(models.Model):
    nombre_distribuidor = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    direccion = models.TextField()    
    ciudad = models.CharField(max_length=100)
    a_domicilio =  models.BooleanField()
    pago_con_tarjeta = models.BooleanField()
    notas = models.TextField(null=True)
    telefono = models.CharField(max_length=20)
    ultima_actualizacion = models.DateTimeField('date updated')


    def __str__(self):
        return self.nombre_distribuidor

class Tanque(models.Model):
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.CASCADE)
    disponibilidad_renta = models.IntegerField()
    disponibilidad_venta = models.IntegerField()
    disponibilidad_recarga = models.IntegerField()
    def __str__(self):
        return "Tanque- " + self.distribuidor.nombre_distribuidor

class Concentrador(models.Model):
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.CASCADE)
    disponibilidad_renta = models.IntegerField()
    disponibilidad_venta = models.IntegerField()
    def __str__(self):
        return "Concentrador- " + self.distribuidor.nombre_distribuidor
