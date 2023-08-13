from django.contrib import admin
from .models import Signup

@admin.register(Signup)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'person_name',
        'person_email',
        'person_pw'
    )
# Register your models here.
