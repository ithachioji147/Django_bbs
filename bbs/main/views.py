from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import PostForm


def index(request):
    articles = Article.objects.all()
    return render(request, 'main/index.html', {'articles': articles})


def new_article(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:index')
    else:
        form = PostForm
    return render(request, 'main/new_article.html', {'form': form})


def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'main/detail.html', {'article': article})


def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('main/index.html')