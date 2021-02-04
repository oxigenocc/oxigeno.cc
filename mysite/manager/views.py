from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse

from oxigeno.models import Distribuidor

def manager_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    data = {'success': True}
                else:
                    data = {'success': False, 'error': 'El usuario fue desactivado'}
            else:
                data = {'success': False, 'error': 'No se pudo autenticar el usuario con esas credenciales'}

            return JsonResponse(data)

    return JsonResponse({"message": "Bad request. Contacta al administrador del sitio"}, status=400)


def manager_logout(request):
    logout(request)
    return JsonResponse({"message": "Log out successful."})


def rest_post(request):
    p = request.POST
    dist = Distribuidor.objects.get(pk=p['distribuidorId'])
    dist.notas = p['notas']

    tanque = dist.tanque_set[0]
    concentrador = dist.concentrador_set[0]

    tanque.ofrece_renta = p['tanqueOfreceRenta']
    tanque.disponibilidad_renta = p['tanqueDisponibilidadRenta']
    tanque.ofrece_venta = p['tanqueOfreceVenta']
    tanque.disponibilidad_venta = p['tanqueDisponibilidadVenta']
    tanque.ofrece_recarga = p['tanqueOfreceRecarga']
    tanque.disponibilidad_recarga = p['tanqueDisponibilidadRecarga']
    concentrador.ofrece_renta = p['concentradorOfreceRenta']
    concentrador.disponibilidad_recarga = p['concentradorDisponibilidadRenta']
    concentrador.ofrece_venta = p['concentradorOfreceVenta']
    concentrador.disponibilidad_venta = p['concentradorDisponibilidadVenta']
    tanque.save()
    concentrador.save()
    dist.save()
