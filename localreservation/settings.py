"""
Django settings for localreservation project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
 STATIC_URL = '/static/'
 STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uq)c_%340g_(kr0%p6*2xwkhv(6+i-x*whxh=21ksw2r5p#0ef'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap_modal_forms',
    'dr.apps.DrConfig',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'localreservation.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'localreservation.wsgi.application'

INDEX_URL = ''
INDEX_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = INDEX_REDIRECT_URL
LOGIN_URL= 'login/'
LOGOUT_URL= 'logout/'
REGISTER_URL = 'signup/'
RESERVATIONS_URL = 'reservations/'
RESERVATION_URL = 'reservation/'
CONCIERGE_URL = 'concierge/'
FAILED_RESERVATION_URL = 'failed_reservation/'
FAILED_REGISTER_URL = 'failed_register/'
PASSWORD_CHANGE_URL = 'password_change'
ABOUT_URL = 'about/'
CONTACT_URL = 'contact/'
PASSWORD_RESET_URL = 'password_reset/'
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# to send mails
# EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # uncomment this line to send mails to your console 
EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST = 'smtp-relay.sendinblue.com' #sendinblue
EMAIL_HOST_USER = 'startapplocha86@gmail.com' #sendinblue / gmail
# EMAIL_HOST_PASSWORD  = '7MfXRwy1IjsPDAQC' #sendinblue
EMAIL_HOST_PASSWORD = 'unistartapp1!' #gmail
EMAIL_USE_TLS = True
EMAIL_PORT = 587
# EMAIL_HOST_USER = 'apikey' #sendgrid
# EMAIL_HOST_PASSWORD = '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' #sendgrid
DEFAULT_FROM_EMAIL = 'testing@testing.com'

BOOTSTRAP4 = {
    'include_jquery': True,
}

#AUTH_USER_MODEL = ' dr.User'