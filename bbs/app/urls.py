from django.urls import path
from django.contrib.auth.views import LoginView
from .import views

app_name = 'app'
urlpatterns = [
    path('login/',
        LoginView.as_view(
            redirect_authenticated_user=True,
            template_name='app/login.html'
        ),
        name='login'),
    path('main/', views.index, name='index'),
    path('<int:post_id>', views.detail, name='detail'),
    path('new_post', views.new_post, name='new_post'),
    path('edit_post', views.edit_post, name='edit_post'),

]
