######################
#   Local commands   #
######################

build:
	cd frontend; npm install; npm run build
	rm -rf mysite/oxigeno/static
	mkdir mysite/oxigeno/static
	cp -r frontend/build mysite/oxigeno/static
	mv mysite/oxigeno/static/static/css mysite/oxigeno/static/css 
	mv mysite/oxigeno/static/static/media mysite/oxigeno/static/media 
	mv mysite/oxigeno/static/static/js mysite/oxigeno/static/js

######################
#    Dev commands    #
######################

collect:
	cd ..; rm -rf static
	source venv/bin/activate; cd mysite; python manage.py collectstatic
	cd ..; tar -czvf static/static.tar.gz static

devdeploy: collect
	docker-compose up --build

######################
#   Prod commands    #
######################

prodeploy:
	rm -rf static
	wget dev-oxigeno.cdmx.gob.mx/static/static.tar.gz
	tar -xf static.tar.gz
	docker-compose up -d