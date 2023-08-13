from django.urls import path
from . import views

urlpatterns = [
    path('', views.mailbox, name='mailbox'),
    path('mail_write/', views.mail_write, name='mail_write'),
    path('mail_read/', views.mail_read, name='mail_read'),
    #path('mail_read/readfunc/', views.readfunc, name='readfunc')
    
]
