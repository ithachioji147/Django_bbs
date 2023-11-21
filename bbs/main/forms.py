from django.forms import ModelForm
from .models import Article


class PostForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'thema', 'text', 'url_link', 'attached_file', 'approved_or_not']