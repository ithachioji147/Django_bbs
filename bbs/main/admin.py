from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'theme')
    list_display_links = ('id', 'title')


# admin.site.register(Article, ArticleAdmin)
admin.site.register(Article)
