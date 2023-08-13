from django.db import models

# Create your models here.

class Signup(models.Model):
    person_name = models.CharField(max_length=16, unique=True, verbose_name = '유저 닉네임', null=True)
    person_email = models.EmailField(max_length=128, unique=True, verbose_name='유저 이메일')
    person_pw = models.CharField(max_length=128, verbose_name='유저 비밀번호')

    def __str__(self):
        return self.person_email
    
    class Meta:
        db_table = 'person'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'