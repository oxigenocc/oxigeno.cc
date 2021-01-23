from django.contrib import admin

# Register your models here.
from .models import Distribuidor, Tanque, Concentrador

admin.site.register(Distribuidor)
admin.site.register(Tanque)
admin.site.register(Concentrador)