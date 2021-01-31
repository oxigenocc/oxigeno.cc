python manage.py makemigrations --skip-checks
python manage.py migrate
gunicorn --bind 0.0.0.0:5000 mysite.wsgi:application
