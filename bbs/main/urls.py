from django.urls import path
from django.contrib.auth.views import LoginView
from .import views

app_name = 'main'
urlpatterns = [
    path('login/',
        LoginView.as_view(
            redirect_authenticated_user=True,
            template_name='main/login.html'
        ),
        name='login'),
    path('', views.index, name='index'),
    path('new_article', views.new_article, name='new_article'),
    path('<int:article_id>', views.detail, name='detail'),
    path('delete_article/<int:article_id>', views.delete_article, name='delete_article'),

]
