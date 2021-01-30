from datetime import datetime as dt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.db.models import Max
from django.core.paginator import Paginator
from django.core.exceptions import FieldError
from decouple import config
import pytz

from .models import Distribuidor, Tanque, Concentrador


def sort_by_availability(dist):
    values = []
    for t in dist['tanques']:
        values += t.values()
    for c in dist['concentradores']:
        values += c.values()
    if values:
        ret = max(values)
    else:
        ret = 0
    return ret



def rest_get(request):
    params = request.GET
    distribuidores = filter_distribuidores(params)
    dist_list = []
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
            'id': d.id,
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
        dist_list.append(data)
    dist_list.sort(reverse=True, key=sort_by_availability)
    if 'page' in params and 'perPage' in params:
        if params['page'].isnumeric() and params['perPage'].isnumeric():
            if int(params['page']) <= 0 or int(params['perPage']) <= 0:
                return JsonResponse({"message": "Page number or perPage is less than or equal to 0"}, status=400)
            if int(params['page']) > p.num_pages:
                return JsonResponse({"message": "Page number is greater than amount of pages."}, status=404)
            p = Paginator(dist_list, int(params['perPage']))
            page = p.page(int(params['page']))
            resp = {
                "links": link_obj_maker(params, page, p, config('DEBUG')),
                "indice": page.end_index(),
                "total": p.count,
                "distribuidores": page.object_list
            }
        else:
            return JsonResponse({"message": "Page number or perPage value is not numeric"}, status=400)
    else:
        resp = {
                    "links": None,
                    "indice": None,
                    "total": None,
                    "distribuidores": dist_list
                }
    return JsonResponse(resp, safe=False)


def filter_distribuidores(q):
    d = Distribuidor.objects.all()
    if not q:
        return d
    if not d:
        return []
    if 'tanqueVenta' in q:
        if not q['tanqueVenta'].isnumeric():
            raise FieldError("tanqueVenta is not an int")
        if int(q['tanqueVenta']):
            d = d.filter(tanque__disponibilidad_venta__gt=0).distinct()
    if 'tanqueRecarga' in q:
        if not q['tanqueRecarga'].isnumeric():
            raise FieldError("tanqueRecarga is not an int")
        if int(q['tanqueRecarga']):
            d = d.filter(tanque__disponibilidad_recarga__gt=0).distinct()
    if 'tanqueRenta' in q:
        if not q['tanqueRenta'].isnumeric():
            raise FieldError("tanqueRenta is not an int")
        if int(q['tanqueRenta']):
            d = d.filter(tanque__disponibilidad_renta__gt=0).distinct()
    if 'concentradorVenta' in q:
        if not q['concentradorVenta'].isnumeric():
            raise FieldError("concentradorVenta is not an int")
        if int(q['concentradorVenta']):
            d = d.filter(concentrador__disponibilidad_venta__gt=0).distinct()
    if 'concentradorRenta' in q:
        if not q['concentradorRenta'].isnumeric():
            raise FieldError("concentradorRenta is not an int")
        if int(q['concentradorRenta']):
            d = d.filter(concentrador__disponibilidad_renta__gt=0).distinct()
    if 'pagoConTarjeta' in q:
        if not q['pagoConTarjeta'].isnumeric():
            raise FieldError("pagoConTarjeta is not an int")
        if int(q['pagoConTarjeta']):
            d = d.filter(pago_con_tarjeta=True).distinct()
    if 'aDomicilio' in  q:
        if not q['aDomicilio'].isnumeric():
            raise FieldError("aDomicilio is not an int")
        if int(q['aDomicilio']):
            d = d.filter(a_domicilio=True).distinct()
    return d


def link_obj_maker(q, page, p, debug):
    este = "https://oxigenocdmx.cc/oxigeno/data?" + q.urlencode() \
            if not debug else "https://dev-oxigeno.cdmx.gob.mx/oxigeno/data?" + q.urlencode()
    prim = q.copy()
    prim['page'] = 1
    primero = "https://oxigenocdmx.cc/oxigeno/data?" + prim.urlencode() \
            if not debug else "https://dev-oxigeno.cdmx.gob.mx/oxigeno/data?" + prim.urlencode()
    ult = q.copy()
    ult['page'] = p.num_pages
    ultimo = "https://oxigenocdmx.cc/oxigeno/data?" + ult.urlencode() \
            if not debug else "https://dev-oxigeno.cdmx.gob.mx/oxigeno/data?" + ult.urlencode()
    if page.has_previous():
        ant = q.copy()
        ant['page'] = page.previous_page_number()
        anterior = "https://oxigenocdmx.cc/oxigeno/data?" + ant.urlencode() \
                if not debug else "https://dev-oxigeno.cdmx.gob.mx/oxigeno/data?" + ant.urlencode()
    else:
        anterior = None
    if page.has_next():
        sig = q.copy()
        sig['page'] = page.next_page_number()
        siguiente = "https://oxigenocdmx.cc/oxigeno/data?" + sig.urlencode() \
                if not debug else "https://dev-oxigeno.cdmx.gob.mx/oxigeno/data?" + sig.urlencode()
    else:
        siguiente = None
    
    return {
            "este": este,
            "primero": primero,
            "ultimo": ultimo,
            "anterior": anterior,
            "siguiente": siguiente
    }
    