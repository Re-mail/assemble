from django.urls import path
from django.conf.urls import include
from . import views

appname = 'signup'
urlpatterns = [
    path('signup', views.signup, name='signup')
]