import json

from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

# Register your models here.
from .models import Distribuidor, Tanque, Concentrador

class DistribuidorAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget(attrs={
            'data-autocomplete-options': json.dumps({ 'types': ['geocode',
            'establishment'], 'componentRestrictions': {
                  'country': 'mexico'
              }
          })
      })},
    }

admin.site.register(Distribuidor, DistribuidorAdmin)
admin.site.register(Tanque)
admin.site.register(Concentrador)