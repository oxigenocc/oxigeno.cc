cd ..; rm -rf static
source venv/bin/activate; cd mysite; python manage.py collectstatic
cd ..; tar -czvf static/static.tar.gz static
docker-compose up --build