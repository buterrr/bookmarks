from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_diaplay = ['user', 'date_of_birth', 'photo']
