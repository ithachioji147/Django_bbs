from pathlib import Path
import os
import re
from configparser import ConfigParser
import django_heroku
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-sh@r--i56you_+%c_4thskfp3!1hmblzwpkl9-&q97!y)xvm%#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR, 'static']


ALLOWED_HOSTS = ['127.0.0.1','localhost']


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


INSTALLED_APPS += [
    'debug_toolbar',
]
