import json

from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from simple_history.admin import SimpleHistoryAdmin
from simple_history import register

from .models import Distribuidor, Tanque, Concentrador

class DistribuidorAdmin(admin.ModelAdmin):
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

register(Distribuidor, DistribuidorAdmin)
admin.site.register(Tanque, SimpleHistoryAdmin)
admin.site.register(Concentrador, SimpleHistoryAdmin)