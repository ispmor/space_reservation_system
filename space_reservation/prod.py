""" Production Settings """

import os
import dj_database_url
from .settings import *

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}


DEBUG = bool(os.getenv('DJANGO_DEBUG', ''))

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', SECRET_KEY)

# your domain(eg. 'app-demo.herokuapp.com')
ALLOWED_HOSTS = ['*']
