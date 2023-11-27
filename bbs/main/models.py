from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone


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
    url_link = models.URLField(blank=True)
    attached_file = models.FileField(
        upload_to='attachment/', 
        null=True, 
        blank=True,
        validators=[validate_file_size]
    )
    url_link = models.URLField(null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='DRAFT',
    )
    created_datetime = models.DateTimeField(auto_now_add=True)
    edited_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'main'


@receiver(pre_save, sender=Article)
def update_edited_datetime(sender, instance, **kwargs):
    if instance.pk is not None:
        original_instance = sender.objects.get(pk=instance.pk)
        if instance == original_instance:
            print(original_instance.edited_datetime)
            return
        
    instance.edited_datetime = timezone.now()

