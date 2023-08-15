from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

app_name = 'user'
urlpatterns = [
    path('register/', views.register, name='register'),
    path("login/", auth_views.LoginView.as_view(template_name="user/login.html"), name="login"),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name= 'logout'), #수정
]