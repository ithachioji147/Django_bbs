from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.conf import settings
from .models import Article
from .forms import ArticleForm
import requests


# トップページ
def index(request):
    # if request.user.is_authenticated:
        articles = Article.objects.filter(status='APPROVED').order_by('-edited_datetime')
        return render(request, 'main/index.html', {'articles': articles})    
    # else:
    #     return redirect('main:login')    


# 記事リストの絞込み表示
def get_filtered_articles(request):
    status = request.GET.get('status', None)
    theme = request.GET.get('theme', None)

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

    return render(request, 'main/list.html', context)


# 新規記事作成画面
def new_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, initial={'status': 'DRAFT'})
        if form.is_valid():
            posted_article = form.save()
            notify_title = posted_article.title
            notification = f'掲示板に記事が投稿されました！承認をお願いします。記事タイトル：{notify_title}'
            send_slack_notification(notification,'staff')
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


# 記事編集画面
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
                    notify_title = article.title
                    notification = f'掲示板に記事が公開されました！記事タイトル：{notify_title}'
                    send_slack_notification(notification, 'general')
                    message = '編集を保存しました。該当の記事が公開となります。'
                else:
                    message = '編集を保存しました。'
            form.save()
            return render(request, 'main/confirmation.html', {'message': message})

    else:
        form = ArticleForm(instance=article)

    return render(request, 'main/edit_article.html', {'form': form, 'article': article})


# 投稿・編集後の確認メッセージ
def confirmation(request):
    message = request.GET.get('message', '')
    context = {'message': message}
    return render(request, 'main:confirmation', context)


# slack連携
def send_slack_notification(message, send_to):
    address = {
        'staff': settings.SLACK_WEBHOOK_URL_STAFF, 
        'general': settings.SLACK_WEBHOOK_URL_GENERAL,
    }

    webhook_url = address[send_to]
    payload = {
        'text': message,
    }
    requests.post(webhook_url, json=payload)
