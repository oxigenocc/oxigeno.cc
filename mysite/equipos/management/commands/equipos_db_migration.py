from django.core.management.base import BaseCommand
from oxigeno.models import Tanque, Concentrador
from equipos.models import Tanque as Tan
from equipos.models import Concentrador as Conc


def migration():
    tanques = Tanque.objects.all()
    concentradores = Concentrador.objects.all()
    for tanque in tanques:
        tanq = tanque.__dict__
        tanq.pop('_state')
        try:
            Tan.objects.get_or_create(**tanq)
        except Exception as e:
            print(str(e))
            print("error en la migracion de Tanque {}".format(
                tanq['id']))
    print('Migracion de Tanques terminada')
    for concen in concentradores:
        con = concen.__dict__
        con.pop('_state')
        try:
            Conc.objects.get_or_create(**con)
        except Exception as e:
            print(str(e))
            print("error en la migracion de concentrador {}".format(
                con['id']))
    print('Migracion de Conentradores terminada')


class Command(BaseCommand):
    help = 'Migracion de modelos de tanque, concentrador a arquitectura v3'

    def handle(self, *args, **options):
        migration()