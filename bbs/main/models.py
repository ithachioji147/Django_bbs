from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from django.utils import timezone


def validate_file_size(value):
    filesize = value.size

    if filesize > 1024 * 1024 * 1:
        raise ValidationError("アップロード可能なファイルサイズを超えています。")


class Article(models.Model):
    THEMES = [
        ('useful', 'お役立ち情報'),
        ('diseases', '病気・障害について'),
        ('learning', '学習情報'),
        ('others', 'その他'),
    ]

    STATUS_CHOICES = [
        ('DRAFT', '未承認'),
        ('APPROVED', '承認済'),
        ('DELETED', '削除済'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=40)
    theme = models.CharField(max_length=100, choices=THEMES)
    text = models.TextField(blank=True)
    attached_file = models.FileField(
        upload_to='attachment/',
        null=True,
        blank=True,
        validators=[validate_file_size]
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        blank=True,
        default='DRAFT',
    )
    created_datetime = models.DateTimeField(default=timezone.now)
    edited_datetime = models.DateTimeField(auto_now=True)
    passcode = models.CharField(blank=True, null=True, max_length=4)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'main'
