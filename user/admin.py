from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
		list_display = (
			'email',
			'username',
   			'password',
		)

		list_display_links = (
			'email',
			'username',
   			'password',
		)