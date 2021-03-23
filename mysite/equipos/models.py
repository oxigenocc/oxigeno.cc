from django.db import models
from simple_history.models import HistoricalRecords
from distribuidores.models import Distribuidor



class MaquinaBaseModel(models.Model):
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.CASCADE)
    ofrece_renta = models.BooleanField(default=True)
    disponibilidad_renta = models.IntegerField()
    ofrece_venta = models.BooleanField(default=True)
    disponibilidad_venta = models.IntegerField()
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True


class Tanque(MaquinaBaseModel):
    ofrece_recarga = models.BooleanField(default=True)
    disponibilidad_recarga = models.IntegerField()

    class Meta:
        db_table = 'tanque'

    def __str__(self):
        return "Tanque - " + self.distribuidor.nombre_distribuidor


class Concentrador(MaquinaBaseModel):

    def __str__(self):
        return "Concentrador - " + self.distribuidor.nombre_distribuidor

    class Meta:
        verbose_name_plural = "concentradores"
        db_table = 'concentrador'

