# oxigeno.cc

Sistema de reportes de disponibilidad de oxigeno en la CDMX. Favor de reportar cualquier bug en la página de [issues](https://github.com/oxigenocc/oxigeno.cc/issues).

## Usa nuestra API gratuita
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/69624bc43b05a92a705a#?env%5Boxigeno_env%5D=W3sia2V5IjoibG9jYWxfdXJsIiwidmFsdWUiOiJodHRwOi8vbG9jYWxob3N0OjgwMDAvIiwiZW5hYmxlZCI6dHJ1ZX0seyJrZXkiOiJwcm9kX3VybCIsInZhbHVlIjoiaHR0cHM6Ly9kZXYtb3hpZ2Vuby5jZG14LmdvYi5teC8iLCJlbmFibGVkIjp0cnVlfV0=)

## ¿Quieres replicar esta página en tu ciudad?
En un servidor que redireccione el puerto 443 al 8000 instala [docker](https://docs.docker.com/engine/install/ubuntu/) y [docker-compose](https://docs.docker.com/compose/install/), crea un archivo docker-compose.yaml y pega lo siguiente:
```
version: "3.9"
   
services:
  db:
    image: postgres
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=mL2nGEh49hG!X # Cambia esta clave a una segura
    volumes:
      - /home/oxigenocc/data-db/:/var/lib/postgresql/data # Cambia oxigenocc por el nombre del usuario de tu host
  web:
    restart: always
    image: oxigenocc/oxigeno.cc:latest
    command: bash -c "./entrypoint.sh"
    environment:
      - SECRET_KEY=<secret_key> # Cambia esto por una generada aquí https://miniwebtool.com/django-secret-key-generator/
      - API_KEY=<google_maps_api_key> # Cambia esto por tu API key de google maps
      - DB_NAME=postgres
      - DB_USER=postgres
      - DB_PASS=MyWeirdPass! # Cambia esta clave por la que pusiste arriba en POSTGRES_PASSWORD
      - DB_HOST=db
      - DB_PORT=5432
      - ALLOWED_HOSTS=oxigenocdmx.cc,www.oxigenocdmx.cc # Cambia esto por el dominio que vas a usar en tu host
      - DEBUG=False
    ports:
      - "8000:8000"
    depends_on:
      - db
```
Copia los archivos dentro de la carpeta [static](static/) en el directorio `~/static` de tu servidor. Ahora sólo tienes que correr el siguiente comando y ay debe de funcionar la página:
```bash
docker-compose up -d
```
Cualquier problema con el despliegue lo puedes poner en [issues](https://github.com/oxigenocc/oxigeno.cc/issues).  
Si no tienes un servidor ya configurado puedes seguir los pasos en la sección de [NGINX](#nginx)

## NGINX
### Generación de certificado y configuración de NGINX en Ubuntu 20 LTS

[Instalar certbot](https://certbot.eff.org/lets-encrypt/ubuntufocal-nginx)

```bash
user@server:~$ sudo snap install core
user@server:~$ sudo snap refresh core
user@server:~$ sudo snap install --classic certbot
user@server:~$ sudo ln -s /snap/bin/certbot /usr/bin/certbot
user@server:~$ sudo apt update

user@server:~$ sudo apt info nginx
user@server:~$ # La versión debe ser 1.18

Package: nginx
Version: 1.18.0-0ubuntu1
Priority: optional
Section: web
Origin: Ubuntu
...

user@server:~$ sudo apt install nginx
user@server:~$ sudo systemctl enable nginx
user@server:~$ sudo reboot
user@server:~$ sudo systemctl status nginx
#### start output ####
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Fri 2021-01-29 03:54:23 UTC; 24s ago
       Docs: man:nginx(8)
    Process: 751 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
    Process: 809 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
   Main PID: 813 (nginx)
      Tasks: 3 (limit: 4620)
     Memory: 9.1M
     CGroup: /system.slice/nginx.service
             ├─813 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
             ├─822 nginx: worker process
             └─823 nginx: worker process
#### end output ####
user@server:~$ sudo mv /etc/nginx/nginx.conf{,.bk}
user@server:~$ sudo vim /etc/nginx/nginx.conf
```

Copiar y pegar el contenido de [aquí](conf/nginx.conf) en "/etc/nginx/nginx.conf" y guarlo

```bash
user@server:~$ sudo vim /etc/nginx/conf.d/domain.conf
user@server:~$ # Pegar este segmento de la configuración en "/etc/nginx/conf.d/domain.conf" y guardarlo
#
server {
    listen      80;
    server_name oxigeno.cc www.oxigeno.cc;

    location / {
        return 301 https://$server_name$request_uri;
    }
}
#
user@server:~$ nginx -t
user@server:~$ nginx -s reload
user@server:~$ sudo certbot certonly --nginx
#### start output ####
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Plugins selected: Authenticator nginx, Installer nginx
Enter email address (used for urgent renewal and security notices)
 (Enter 'c' to cancel): email@oxigeno.cc

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Please read the Terms of Service at
https://letsencrypt.org/documents/LE-SA-v1.2-November-15-2017.pdf. You must
agree in order to register with the ACME server. Do you agree?
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: Y

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Would you be willing, once your first certificate is successfully issued, to
share your email address with the Electronic Frontier Foundation, a founding
partner of the Let's Encrypt project and the non-profit organization that
develops Certbot? We'd like to send you email about our work encrypting the web,
EFF news, campaigns, and ways to support digital freedom.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: N
Account registered.

Which names would you like to activate HTTPS for?
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1: oxigeno.cc
2: www.oxigeno.cc
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Select the appropriate numbers separated by commas and/or spaces, or leave input
blank to select all options shown (Enter 'c' to cancel): <PRESS ENTER>
#### end output ####
```

```bash
user@server:~$ sudo mv /etc/nginx/conf.d/domain.conf{.bk}
user@server:~$ sudo vim /etc/nginx/conf.d/domain.conf
```

[Copiar y pegar el contenido de aquí en "/etc/nginx/conf.d/domain.conf" remplaza el nombre del dominio y guardalo](conf/oxigenocc.conf)

```bash
user@server:~$ # Correr el test de las configuraciones y recargarlas
user@server:~$ sudo nginx -t
user@server:~$ sudo nginx -s reload
```

## Django
### Modelos
* Distribuidor:
  - id:
    * AutoField:
      - primary_key=True
  - nombre_distribuidor:
    * CharField:
      - max_length=100
  - horario:
    * CharField:
      - max_length=100
  - estado:
    * CharField:
      - max_length=50
  - direccion:
    * TextField
  - ciudad:
    * CharField:
      - max_length=100
  - a_domicilio:
    * BooleanField
  - pago_con_tarjeta:
    * BooleanField
  - notas:
    * TextField:
      - null=True
      - blank=True
  - notas_internas:
    * TextField:
      - null=True, 
      - blank=True
  - telefono:
    * CharField:
      - max_length=20
  - whatsapp:
    * CharField:
      - max_length=20
      - null=True
      - blank=True
  - link_pagina:
    * CharField:
      - max_length=100
      - null=True
      - blank=True
  - address:
    * AddressField:
      - max_length=200
      - default=''
  - geolocation:
    * GeoLocationField:
      - max_length=100
      - default=''
  - dar_de_baja:
    * BooleanField:
      - default=False
  - fecha_creacion:
    * DateTimeField:
      - auto_now_add=True
  - ultima_actualizacion:
    * DateTimeField:
      - auto_now=True
  - abre_sabado:
    * BooleanField:
      - default=True
  - abre_domingo:
    * BooleanField:
      - default=True
  - abre_24h:
    * BooleanField:
      - default=True
  - recarga_gratis:
    * BooleanField:
      - default=True
  - history:
    * simple_history.models.HistoricalRecords
  
* Tanque:
  - id:
    * AutoField:
      - primary_key=True
  - distribuidor:                   
    * ForeignKey:
        - Distribuidor
        - on_delete=models.CASCADE
  - ofrece_renta:
    * BooleanField:
      - default=True
  - disponibilidad_renta:
    * IntegerField
  - ofrece_venta:
    * BooleanField:
      - default=True
  - disponibilidad_venta
    * IntegerField
  - ofrece_recarga:
    * BooleanField:
      - default=True
  - disponibilidad_recarga:
    * IntegerField
  - ultima_actualizacion:
    * DateTimeField:
      - auto_now=True
  - fecha_creacion:
    * DateTimeField:
      - auto_now_add=True
  - history:
    * simple_history.models.HistoricalRecords
  
* Concentrador:
  - id:
    * AutoField:
      - primary_key=True
  - distribuidor:                   
    * ForeignKey:
        - Distribuidor
        - on_delete=models.CASCADE
  - ofrece_renta:
    * BooleanField:
      - default=True
  - disponibilidad_renta:
    * IntegerField
  - ofrece_venta:
    * BooleanField:
      - default=True
  - disponibilidad_venta
    * IntegerField
  - ultima_actualizacion:
    * DateTimeField:
      - auto_now=True
  - fecha_creacion:
    * DateTimeField:
      - auto_now_add=True
  - history:
    * simple_history.models.HistoricalRecords
  
* DistribuidorPotencial:
  - id:
    * AutoField:
      - primary_key=True
  - nombre_distribuidor:
    * CharField:
      - max_length=100
  - rfc:
    * CharField:
      - max_length=13
  - telefono:
    * CharField:
      - max_length=20
  - direccion:
    * TextField
  - horario:
    * CharField:
      - max_length=100
  - link_pagina:
    * CharField:
      - max_length=100
      - null=True
      - blank=True
  - whatsapp:
    * CharField:
      - max_length=20
      - null=True
      - blank=True
  - a_domicilio:
    * BooleanField
  - pago_con_tarjeta:
    * BooleanField
  - ofrece_venta_de_tanque:
    * BooleanField
  - ofrece_renta_de_tanque:
    * BooleanField
  - ofrece_recarga_de_tanque:
    * BooleanField
  - ofrece_venta_de_concentrador:
    * BooleanField
  - ofrece_renta_de_concentrador:
    * BooleanField
  - notas_internas:
    * TextField:
      - null=True, 
      - blank=True
  - fecha_creacion:
    * DateTimeField:
      - auto_now_add=True
  - ultima_actualizacion:
    * DateTimeField:
      - auto_now=True
  - history:
    * simple_history.models.HistoricalRecords

  
  
## Frontend

[I'm an inline-style link](https://www.google.com)

Contribuidores:
* Uri Goldberg Kleiman: [klaymond](https://github.com/klaymond)
* Alexis Guerrero: [dstprojects](https://github.com/dstprojects)
* Lorenzo Torres: https://github.com/lorenzoajt 
* Alexis Flores: https://github.com/AlexisFlores17
* Jorge García: https://github.com/jorg-gr
* Lopsan: [LopsanAMO](https://github.com/LopsanAMO)

Este proyecto no se pudo lograr sin el esfuerzo e iniciativa de Naoli García. El apoyo de las siguintes personas e instituciones fue indispensable:
* Diana Urquiza
* Mauro Herrera
* Mijael Gutiérrez
* Leonardo Morales
* Geóg. Alejandro Díaz Ponce
* LSD Lab
* Agencia Digital de Innovación Pública de la CDMX
* Tec de Monterrey

