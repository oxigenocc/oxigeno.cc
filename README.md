# oxigeno.cc

Sistema de reportes de disponibilidad de oxigeno en la CDMX

# Generación de certificado y configuración de NGINX en Ubuntu 20 LTS

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

[Copiar y pegar el contenido de aquí en "/etc/nginx/nginx.conf" y guarlo](conf/nginx.conf)

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
