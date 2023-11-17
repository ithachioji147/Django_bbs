from django.db import models


class Article(models.Model):
    THEMAS = (
        ('useful','お役立ち情報'),
        ('diseases','病気・障害について'),
        ('learning','学習情報'),
        ('others','その他'),
    )

    title = models.CharField(blank=False, null=False, max_length=200)
    name = models.CharField(blank=False, null=False, max_length=40)
    thema = models.CharField(max_length=100, choices=THEMAS, blank=False, null=False)
    text = models.TextField()
    url_link = models.URLField()
    attached_file = models.FileField()
    approved_or_not = models.BooleanField(default=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    edited_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'app'