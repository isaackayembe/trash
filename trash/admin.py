from django.contrib import admin
from .models import*

# Register your models here.
@admin.register(Client)
class UserClient(admin.ModelAdmin):
    pass