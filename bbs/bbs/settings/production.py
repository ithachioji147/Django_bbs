import os
from .base import *
import dj_database_url
# from pathlib import Path
# import re
from configparser import ConfigParser
# import django_heroku


DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')


ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']


# 静的ファイルはWhitenoiseを使用

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# STATIC_URL = 'static/'
# STATICFILES_DIRS = [BASE_DIR, 'static']


# データベースはHerokuのPostogresを使用

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}


# メディアファイルはAWS S3を使用
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_REGION_NAME = 'ap-northeast-1'
AWS_STORAGE_BUCKET_NAME = 'hachioji147-bbs-storage'

# アクセスキー
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

MEDIA_URL = 'https://hachioji147-bbs-storage.s3.amazonaws.com/'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'
