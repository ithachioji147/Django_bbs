import os
import dj_database_url
from .base import *


DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']


# データベースはHerokuのPostogresを使用

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}


# 静的ファイルはWhitenoiseを使用

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'
# 下記記述があるとデプロイ時のcollectstaticが失敗する？
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# メディアファイルはAWS S3を使用
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME', 'ap-northeast-1')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/'
# AWSアクセスキー
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')


# Slack通知用のWebhook
SLACK_WEBHOOK_URL_STAFF = os.environ.get('WEBHOOK_STAFF_URL')
SLACK_WEBHOOK_URL_GENERAL = os.environ.get('WEBHOOK_GENERAL_URL')
