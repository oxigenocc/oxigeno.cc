#!/bin/bash
cd ..
rm -rf static
cd oxigeno.cc
source venv/bin/activate
cd mysite
python manage.py collectstatic
cd ../..
tar -czvf static/static.tar.gz static
cd oxigeno.cc
docker-compose up --build