rm -rf static
wget dev-oxigeno.cdmx.gob.mx/static/static.tar.gz
tar -xf static.tar.gz
docker-compose pull
docker-compose up --scale web=5