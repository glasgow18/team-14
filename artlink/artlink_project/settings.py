# DOC Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from keys import *

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# TODO what's the difference between those two? @all
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR, ]

# Dynamic pathing to the templates folder
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

STATIC_URL = '/static/'

# SECURITY WARNING: keep the secret key used in production secret!
# in keys.py file
SECRET_KEY = django_key

# SECURITY WARNING: don't run with debug turned on in production!
# TODO add 404 page to be able to turn Debug to False
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

# bootstrap installed with django to fasten beautify
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'artlink',
    'bootstrap4',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'artlink_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                # 'artlink.context_processors.user',
            ],
        },
    },
]

WSGI_APPLICATION = 'artlink_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
