from django.db import models
from user.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class UserRemail(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    remail = models.EmailField(max_length=255, unique=True)
    
    def __str__(self):
        return self.remail

class Category(models.Model):
    user_remail = models.OneToOneField(UserRemail, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category