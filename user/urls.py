from django.urls import path
from django.conf.urls import include
from . import views

appname = 'user'
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
]