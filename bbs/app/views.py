from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import PostForm


def index(request):
    articles = Article.objects.all().order_by('-created_datetime')
    return render(request, 'app/index.html', {'articles': articles})


def detail(request, post_id):
    article = get_object_or_404(Article, id=post_id)
    return render(request, 'app/detail.html', {'article': article})


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:index')
    else:
        form = PostForm
    return render(request, 'app/new_post.html', {'form':form})


def edit_post(request):
    return render(request, '')


