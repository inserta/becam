from .base import *
import os
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': os.environ['MYSQL_DB'],
        'USER': os.environ['MYSQL_USER'],
        'PASSWORD': os.environ['MYSQL_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': '3306',
    }
}

STATIC_ROOT = "/var/www/becam.com/"
MEDIA_URL = ''