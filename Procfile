web: gunicorn space_reservation.wsgi
release: python manage.py migrate

python manage.py makemigrations
python manage.py migrate
python manage.py runserver