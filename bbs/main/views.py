from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.urls import reverse
# from django.contrib import messages
from .models import Article
from .forms import ArticleForm


def index(request):
    if request.user.is_authenticated:
    #     if request.user.is_staff:
    #         articles = Article.objects.all().order_by('-edited_datetime')
    #     else:
        articles = Article.objects.filter(status='APPROVED').order_by('-edited_datetime')
        return render(request, 'main/index.html', {'articles': articles})
    
    else:
        return redirect('main:login')    


def get_filtered_articles(request):  # 記事一覧をプルダウンで絞り込む
    status = request.GET.get('status', None)
    print(f'status={status}')  # デバッグ用
    theme = request.GET.get('theme', None)
    print(f'theme={theme}')  # デバッグ用

    if status != 'all' and theme != 'all':
        filtered_articles = Article.objects.filter(status=status, theme=theme).order_by('-edited_datetime')
    elif status != 'all':
        filtered_articles = Article.objects.filter(status=status).order_by('-edited_datetime')
    elif theme != 'all':
        filtered_articles = Article.objects.filter(theme=theme).order_by('-edited_datetime')
    else:
        filtered_articles = Article.objects.all().order_by('-edited_datetime')

    context = {'articles': filtered_articles}

    if not filtered_articles.exists():
        context['no_results_message'] = '条件に合致する記事は見つかりませんでした。'

    print(context)  # デバッグ用

    return render(request, 'main/list.html', context)


def new_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, initial={'status': 'DRAFT'})
        if form.is_valid():            
            form.save()
            message = '投稿が完了しました。スタッフの承認後、投稿した記事が公開となります。'
            return render(request, 'main/confirmation.html', {'message': message})
    else:
        form = ArticleForm
    return render(request, 'main/new_article.html', {'form': form})


def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'main/detail.html', {'article': article})


@require_POST
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.status = 'DELETED'
    article.save()
    message = '該当の記事を一覧から削除しました（データは残っているため復旧は可能です）。'
    return render(request, 'main/confirmation.html', {'message': message})


def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        # if form.has_changed():  # JSでボタン制御するため不要
        if form.is_valid():
            if not request.user.is_staff:
                article.status = 'DRAFT'
                message = '編集を保存しました。スタッフの承認後、編集後の記事が公開となります。'
            else:
                if article.status == 'APPROVED':
                    message = '編集を保存しました。該当の記事が公開となります。'
                else:
                    message = '編集を保存しました。'
            form.save()
            return render(request, 'main/confirmation.html', {'message': message})
            
        # return redirect('main:index')
    else:
        form = ArticleForm(instance=article)


    return render(request, 'main/edit_article.html', {'form': form, 'article': article})


def confirmation(request):
    message = request.GET.get('message', '')
    context = {'message': message}
    return render(request, 'main:confirmation', context)
