from django.forms import ModelForm
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'theme', 'text', 'url_link', 'attached_file', 'approved_or_not']