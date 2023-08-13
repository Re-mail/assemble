from django.db import models

# Create your models here.

class Address(models.Model):
    address_remail = models.EmailField(max_length=128, unique=True, verbose_name='생성 주소')
    address_category = models.CharField(max_length=32, unique=True, verbose_name='생성 주소 카테고리')
    
    def __str__(self):
        return self.address_remail
    
    class Meta:
        db_table = 'address'
        verbose_name = 'remail 주소'
        verbose_name_plural = 'remail 주소'