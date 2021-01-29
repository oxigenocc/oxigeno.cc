from datetime import datetime as dt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.db.models import Max
import pytz

from .models import Distribuidor, Tanque, Concentrador


def sort_by_availability(dist):
    values = []
    for t in dist['tanques']:
        values += t.values()
    for c in dist['concentradores']:
        values += c.values()
    return max(values)



def rest_get(request):
    distribuidores = Distribuidor.objects.all()
    resp = []
    for d in distribuidores:
        tanques = [
            {
                'disponibilidad_renta': x.disponibilidad_renta,
                'disponibilidad_venta': x.disponibilidad_venta,
                'disponibilidad_recarga': x.disponibilidad_recarga
            } for x in d.tanque_set.all()
        ]
        concentradores = [
            {
                'disponibilidad_renta': x.disponibilidad_renta,
                'disponibilidad_venta': x.disponibilidad_venta
            } for x in d.concentrador_set.all()
        ]

        max_tanque = max(tanque.ultima_actualizacion for tanque in d.tanque_set.all()) if d.tanque_set.all() else dt.min.replace(tzinfo=pytz.UTC)
        max_concentrador = max(concentrador.ultima_actualizacion for concentrador in d.concentrador_set.all()) if d.concentrador_set.all() else dt.min.replace(tzinfo=pytz.UTC)
        ultima_actualización = max([d.ultima_actualizacion, max_tanque, max_concentrador]) 

        location = str(d.geolocation).split(',')

        data = {
            'nombre_distribuidor': d.nombre_distribuidor,
            'horario': d.horario,
            'estado': d.estado,
            'direccion': d.direccion,
            'ciudad': d.ciudad,
            'a_domicilio': d.a_domicilio,
            'pago_con_tarjeta': d.pago_con_tarjeta,
            'notas': d.notas,
            'telefono': d.telefono,
            'ultima_actualizacion': ultima_actualización,
            'concentradores': concentradores,
            'tanques': tanques,
            'lat': location[0],
            'lng': location[1],
        }
        resp.append(data)
    data.sort(key=sort_by_availability)
    return JsonResponse(resp, safe=False)


