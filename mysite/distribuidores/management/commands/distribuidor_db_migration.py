from django.core.management.base import BaseCommand
from oxigeno.models import Distribuidor, DistribuidorPotencial
from distribuidores.models import Distribuidor as Distrib
from distribuidores.models import DistribuidorPotencial as DistribPot
from distribuidores.models import Estado


def migration(estado):
    estado, c = Estado.objects.get_or_create(nombre=estado)
    distribuidores = Distribuidor.objects.all()
    distribuidores_poten = DistribuidorPotencial.objects.all()
    for distribuidor in distribuidores:
        distri = distribuidor.__dict__
        distri.pop('_state')
        distri['estado_procedencia'] = estado
        distri['nombre'] = distri['nombre_distribuidor']
        distri.pop('nombre_distribuidor')
        try:
            Distrib.objects.get_or_create(**distri)
        except Exception as e:
            print(str(e))
            print("error en la migracion de distribuidor {}".format(
                distri['id']))
    print('Migracion de distribuidores terminada')
    for potencial in distribuidores_poten:
        pot = potencial.__dict__
        pot.pop('_state')
        pot['nombre'] = pot['nombre_distribuidor']
        pot['estado_procedencia'] = estado
        pot.pop('nombre_distribuidor')
        try:
            DistribPot.objects.get_or_create(**pot)
        except Exception as e:
            print(str(e))
            print("error en la migracion de distribuidor potencial {}".format(
                pot['id']))
    print('Migracion de distribuidores potenciales terminada')


class Command(BaseCommand):
    help = 'Migracion de modelos de distribuidor a arquitectura v3'

    def add_arguments(self, parser):
        parser.add_argument('estado', type=str)

    def handle(self, *args, **options):
        print(options)
        estado = options['estado']
        migration(estado)