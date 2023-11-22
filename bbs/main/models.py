from django.core.exceptions import ValidationError
from django.db import models


def validate_file_size(value):
    filesize = value.size
    
    if filesize > 1024 * 1024 * 1:
        raise ValidationError("アップロード可能なファイルサイズを超えています。")


class Article(models.Model):
    THEMAS = (
        ('useful', 'お役立ち情報'),
        ('diseases', '病気・障害について'),
        ('learning', '学習情報'),
        ('others', 'その他'),
    )

    STATUS_CHOICES = [
        ('UNAPPROVED', '未承認'),
        ('APPROVED', '承認済'),
        ('DELETED', '削除済'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=40)
    thema = models.CharField(max_length=100, choices=THEMAS)
    text = models.TextField(blank=True)
    url_link = models.URLField(blank=True)
    attached_file = models.FileField(
        upload_to='attachment/', 
        null=True, 
        blank=True,
        validators=[validate_file_size]
    )
    url_link = models.URLField(null=True, blank=True)
    approved_or_not = models.BooleanField(default=False)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='UNAPPROVED',
    )
    created_datetime = models.DateTimeField(auto_now_add=True)
    edited_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'main'
