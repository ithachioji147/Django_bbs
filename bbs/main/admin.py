from django.contrib import admin
# from .models import Article
from .models import Article, Theme


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'theme')
    list_display_links = ('id', 'title')


class ThemeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'label')

# admin.site.register(Article, ArticleAdmin)
admin.site.register(Article)
admin.site.register(Theme)