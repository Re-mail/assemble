from django.urls import path
from django.conf.urls import include
from . import views

appname = 'mypage'
urlpatterns = [
    path('', views.mypage, name='mypage'),
    path('new_address', views.new_address, name='new_address')
]