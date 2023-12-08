from pathlib import Path
import os
import re
from configparser import ConfigParser
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'whitenoise.runserver_nostatic',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'main.middleware.restrict_access.RestrictAccessMiddleware',
]

ROOT_URLCONF = 'bbs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
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

WSGI_APPLICATION = 'bbs.wsgi.application'




# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_TZ = True



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



####################################
# 以下、追加部分
####################################

LOGIN_REDIRECT_URL = '/'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'

SESSION_COOKIE_AGE = 14 * 24 * 60 * 60


# ログインしていない状態でアクセスできるパス
ALLOWED_PATHS = [
    '/login/',
    '/admin/'
]


# 以下は設定ファイル（config.ini）から読み込む --- localのみ
# config = ConfigParser()
# config.read('config.ini')

# SlackのWebhook --- local時の設定
# SLACK_WEBHOOK_URL_STAFF = config.get('WEBHOOK_STAFF', 'URL')
# SLACK_WEBHOOK_URL_GENERAL = config.get('WEBHOOK_GENERAL', 'URL')

# SlackのWebhook --- 本番環境は環境変数を使用
SLACK_WEBHOOK_URL_STAFF = os.environ.get('WEBHOOK_STAFF_URL')
SLACK_WEBHOOK_URL_GENERAL = os.environ.get('WEBHOOK_GENERAL_URL')

# NGROKで発行する一時的なアドレス
# ALLOWED_HOSTS = ['localhost', config.get('NGROK', 'HOST')]
# CSRF_TRUSTED_ORIGINS = [config.get('NGROK', 'FULL_URL')]

django_heroku.settings(locals())
