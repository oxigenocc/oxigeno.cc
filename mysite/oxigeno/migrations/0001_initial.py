# Generated by Django 3.1.5 on 2021-02-04 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_google_maps.fields
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Distribuidor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_distribuidor', models.CharField(max_length=100)),
                ('horario', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=50)),
                ('direccion', models.TextField()),
                ('ciudad', models.CharField(max_length=100)),
                ('a_domicilio', models.BooleanField()),
                ('pago_con_tarjeta', models.BooleanField()),
                ('notas', models.TextField(blank=True, null=True)),
                ('telefono', models.CharField(max_length=20)),
                ('whatsapp', models.CharField(blank=True, max_length=20, null=True)),
                ('link_pagina', models.CharField(blank=True, max_length=100, null=True)),
                ('address', django_google_maps.fields.AddressField(default='', max_length=200)),
                ('geolocation', django_google_maps.fields.GeoLocationField(default='', max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'distribuidores',
            },
        ),
        migrations.CreateModel(
            name='Tanque',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('disponibilidad_renta', models.IntegerField()),
                ('disponibilidad_venta', models.IntegerField()),
                ('disponibilidad_recarga', models.IntegerField()),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('distribuidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oxigeno.distribuidor')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalTanque',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('disponibilidad_renta', models.IntegerField()),
                ('disponibilidad_venta', models.IntegerField()),
                ('disponibilidad_recarga', models.IntegerField()),
                ('ultima_actualizacion', models.DateTimeField(blank=True, editable=False)),
                ('fecha_creacion', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('distribuidor', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='oxigeno.distribuidor')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical tanque',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDistribuidor',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('nombre_distribuidor', models.CharField(max_length=100)),
                ('horario', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=50)),
                ('direccion', models.TextField()),
                ('ciudad', models.CharField(max_length=100)),
                ('a_domicilio', models.BooleanField()),
                ('pago_con_tarjeta', models.BooleanField()),
                ('notas', models.TextField(blank=True, null=True)),
                ('telefono', models.CharField(max_length=20)),
                ('whatsapp', models.CharField(blank=True, max_length=20, null=True)),
                ('link_pagina', models.CharField(blank=True, max_length=100, null=True)),
                ('address', django_google_maps.fields.AddressField(default='', max_length=200)),
                ('geolocation', django_google_maps.fields.GeoLocationField(default='', max_length=100)),
                ('fecha_creacion', models.DateTimeField(blank=True, editable=False)),
                ('ultima_actualizacion', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical distribuidor',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalConcentrador',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('disponibilidad_renta', models.IntegerField()),
                ('disponibilidad_venta', models.IntegerField()),
                ('ultima_actualizacion', models.DateTimeField(blank=True, editable=False)),
                ('fecha_creacion', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('distribuidor', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='oxigeno.distribuidor')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical concentrador',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Concentrador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('disponibilidad_renta', models.IntegerField()),
                ('disponibilidad_venta', models.IntegerField()),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('distribuidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oxigeno.distribuidor')),
            ],
            options={
                'verbose_name_plural': 'concentradores',
            },
        ),
    ]