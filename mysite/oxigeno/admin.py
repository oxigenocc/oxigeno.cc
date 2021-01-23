from django.contrib import admin

# Register your models here.
from models import Distrubuidor, Tanque, Concentrador

admin.site.register(Distrubuidor)
admin.site.register(Tanque)
admin.site.register(Concentrador)