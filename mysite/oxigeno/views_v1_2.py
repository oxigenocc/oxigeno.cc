from datetime import datetime as dt
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core.exceptions import FieldError
from django.views.decorators.csrf import csrf_exempt
from decouple import config
import pytz

from .models import Distribuidor, DistribuidorPotencial


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
                'renta': x.ofrece_renta,
                'disponibilidad_renta': x.disponibilidad_renta,
                'venta': x.ofrece_venta,
                'disponibilidad_venta': x.disponibilidad_venta,
                'recarga': x.ofrece_recarga,
                'disponibilidad_recarga': x.disponibilidad_recarga
            } for x in d.tanque_set.all()
        ]
        concentradores = [
            {                
                'renta': x.ofrece_renta,
                'disponibilidad_renta': x.disponibilidad_renta,
                'venta': x.ofrece_venta,
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
            'whatsapp': d.whatsapp,
            'link_pagina': d.link_pagina
        }
        dist_list.append(data)
    dist_list.sort(reverse=True, key=sort_by_availability)
    if 'page' in params and 'perPage' in params:
        if params['page'].isnumeric() and params['perPage'].isnumeric():
            if int(params['page']) <= 0 or int(params['perPage']) <= 0:
                return JsonResponse({"message": "Page number or perPage is less than or equal to 0"}, status=400)
            p = Paginator(dist_list, int(params['perPage']))
            if int(params['page']) > p.num_pages:
                return JsonResponse({"message": "Page number is greater than amount of pages."}, status=404)
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
    if 'incluirBajas' in q:
        if not q['incluirBajas'].isnumeric():
            raise FieldError("incluirBajas is not an int")
        if not int(q['incluirBajas']):
            d = d.filter(dar_de_baja=False).distinct()
    else:
        d = d.filter(dar_de_baja=False).distinct()
    if 'nombreComo' in q:
        d = d.filter(nombre_distribuidor__unaccent__icontains=q['nombreComo']).distinct()
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



def rest_get_single(request, id_distribuidor):
    try:
        d = Distribuidor.objects.get(pk=id_distribuidor)
    except Distribuidor.DoesNotExist:
        return JsonResponse({"message": "Distribuidor no encontrado"}, status=404)
    
    tanques = [
        {
            'renta': x.ofrece_renta,
            'disponibilidad_renta': x.disponibilidad_renta,
            'venta': x.ofrece_venta,
            'disponibilidad_venta': x.disponibilidad_venta,
            'recarga': x.ofrece_recarga,
            'disponibilidad_recarga': x.disponibilidad_recarga
        } for x in d.tanque_set.all()
    ]
    concentradores = [
        {                
            'renta': x.ofrece_renta,
            'disponibilidad_renta': x.disponibilidad_renta,
            'venta': x.ofrece_venta,
            'disponibilidad_venta': x.disponibilidad_venta
        } for x in d.concentrador_set.all()
    ]

    max_tanque = max(tanque.ultima_actualizacion for tanque in d.tanque_set.all()) if d.tanque_set.all() else dt.min.replace(tzinfo=pytz.UTC)
    max_concentrador = max(concentrador.ultima_actualizacion for concentrador in d.concentrador_set.all()) if d.concentrador_set.all() else dt.min.replace(tzinfo=pytz.UTC)
    ultima_actualización = max([d.ultima_actualizacion, max_tanque, max_concentrador]) 

    location = str(d.geolocation).split(',')
    resp = {
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
            'whatsapp': d.whatsapp,
            'link_pagina': d.link_pagina,
            'baja': d.dar_de_baja,
        }
    return JsonResponse(resp)
    

@csrf_exempt
def rest_post_distribuidor_potencial(request):
    data = request.POST
    if request.method == 'POST':
        d = DistribuidorPotencial(
            nombre_distribuidor=data.get('nombreDistribuidor'),
            rfc=data.get('rfc'),
            telefono=data.get('telefono'),
            direccion=data.get('direccion'),
            horario=data.get('horario'),
            link_pagina=data.get('linkPagina'),
            whatsapp=data.get('whatsapp'),
            a_domicilio=data.get('aDomicilio'),
            pago_con_tarjeta=data.get('pagoConTarjeta'),
            ofrece_venta_de_tanque=data.get('ofreceVentaDeTanque'),
            ofrece_renta_de_tanque=data.get('ofreceRentaDeTanque'),
            ofrece_recarga_de_tanque=data.get('ofreceRecargaDeTanque'),
            ofrece_venta_de_concentrador=data.get('ofreceVentaDeConcentrador'),
            ofrece_renta_de_concentrador=data.get('ofreceRentaDeConcentrador')
        )
        d.save()
        return JsonResponse({"message": "Succesfully saved distribuidor potencial"})
    else:
        return JsonResponse({"message": "The request should be POST"}, status=400)
