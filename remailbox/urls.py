from django.urls import path
from . import views

urlpatterns = [
    path('', views.mailbox),
    path('mail_write/', views.mail_write),
    path('mail_read/', views.mail_read),
]
