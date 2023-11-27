from django.forms import ModelForm
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'theme', 'text', 'attached_file']

    # def has_changed(self):
    #     return super().has_changed()