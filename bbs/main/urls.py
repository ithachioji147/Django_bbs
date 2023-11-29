from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'
urlpatterns = [
    path('login/', LoginView.as_view(redirect_authenticated_user=True, template_name='main/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('', views.index, name='index'),
    path('list/', views.get_filtered_articles, name='get_filtered_articles'),
    path('new_article', views.new_article, name='new_article'),
    path('<int:article_id>', views.detail, name='detail'),
    path('delete_article/<int:article_id>', views.delete_article, name='delete_article'),
    path('edit_article/<int:article_id>', views.edit_article, name='edit_article'),
    path('confirmation/', views.confirmation, name='confirmation'),

]

# デバッグモード
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
