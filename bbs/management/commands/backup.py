from django.core.management.base import BaseCommand
import boto3
from django.conf import settings


class Command(BaseCommand):
    help = 'Uploads a file to AWS S3'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)
        parser.add_argument('s3_file_path', type=str)

    def handle(self, *args, **options):
        file_path = options['file_path']
        s3_file_path = options['s3_file_path']
        self.stdout.write(self.style.SUCCESS(f'Uploading {file_path} to S3 at {s3_file_path}...'))

        s3 = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )
        bucket_name = settings.AWS_STORAGE_BUCKET_NAME

        with open(file_path, 'rb') as data:
            s3.upload_fileobj(data, bucket_name, s3_file_path)

        self.stdout.write(self.style.SUCCESS('Successfully uploaded to S3!'))
