from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import datetime


# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, username, password=None):

        if not email:
            raise ValueError('must have user email')
        if not username:
            raise ValueError('must have user username')

        user = self.model(
            email=email,
            username=username,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):

        user = self.create_user(
            email=email,
            username = username,
  
        )
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):

    objects = UserManager()

    email = models.EmailField(max_length=255, unique=True, null = True, default="")
    username = models.CharField(max_length=10, null = True, default="")
    password = models.CharField(max_length=255, null = True, default="")
    is_active = models.BooleanField(default=True, null = True)
    is_admin = models.BooleanField(default=False, null = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.username)

    @property
    def is_staff(self):
        return self.is_admin
