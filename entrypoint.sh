python manage.py populate_history --auto
python manage.py makemigrations --skip-checks
python manage.py migrate
gunicorn --bind 0.0.0.0:8000 mysite.wsgi:application