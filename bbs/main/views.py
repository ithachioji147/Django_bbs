from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Article
from .forms import ArticleForm


def index(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            articles = Article.objects.all().order_by('-edited_datetime')
        else:
            articles = Article.objects.filter(status='APPROVED').order_by('-edited_datetime')

        status_filter = request.GET.get('status', '')
        if status_filter != 'all':
            articles = Article.objects.filter(status=status_filter).order_by('-edited_datetime')
        else:
            articles = Article.objects.all().order_by('-edited_datetime')

        return render(request, 'main/index.html', {'articles': articles, 'status_filter': status_filter})
    else:
        return redirect('main:login')    


def get_filtered_articles(request):
    status = request.GET.get('status', 'APPROVED')
    print(status)
    theme = request.GET.get('tehme', 'OTHERS')
    print(theme)
    filterd_articles = Article.objects.filter(status=status, theme=theme)
    print(filterd_articles)
    return render(request, 'main/list.html', {'articles':filterd_articles})



def new_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:index')
    else:
        form = ArticleForm
    return render(request, 'main/new_article.html', {'form': form})


def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'main/detail.html', {'article': article})


@require_POST
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('main:index')

def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('main:index')
    else:
        form = ArticleForm(instance=article)

    return render(request, 'main/edit_article.html', {'form': form, 'article': article})
