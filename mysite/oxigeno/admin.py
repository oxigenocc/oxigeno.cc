import json

from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from simple_history.admin import SimpleHistoryAdmin
from simple_history import register

from .models import Distribuidor, Tanque, Concentrador


class DistribuidorAdmin(SimpleHistoryAdmin):

    
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('nombre_distribuidor')
            self.exclude.append('horario')
            self.exclude.append('estado')
            self.exclude.append('direccion')
            self.exclude.append('ciudad')
            self.exclude.append('a_domicilio')
            self.exclude.append('pago_con_tarjeta')
            self.exclude.append('telefono')
            self.exclude.append('whatsapp')
            self.exclude.append('link_pagina')
            self.exclude.append('address')
            self.exclude.append('geolocation')
        return super(DistribuidorAdmin, self).get_form(request, obj, **kwargs)

    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget(attrs={
            'data-autocomplete-options': json.dumps({ 'types': 
                                                        ['geocode', 'establishment'], 
                                                    'componentRestrictions': {
                                                        'country': 'mx'
                                                    }
          })
      })},
    }


class TanqueAdmin(SimpleHistoryAdmin):
    
    
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('distribuidor')
        return super(TanqueAdmin, self).get_form(request, obj, **kwargs)


class ConcentradorAdmin(SimpleHistoryAdmin):
    
    
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('distribuidor')
        return super(ConcentradorAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(Distribuidor, DistribuidorAdmin)
admin.site.register(Tanque, TanqueAdmin)
admin.site.register(Concentrador, ConcentradorAdmin)