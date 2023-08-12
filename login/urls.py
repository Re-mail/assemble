from django.urls import path
from django.conf.urls import include
from . import views

appname = 'login'
urlpatterns = [
    path('login', views.login, name='login')
]