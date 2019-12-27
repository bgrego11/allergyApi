from django.contrib import admin
from .models import Food, Ingredient, LogEntry

@admin.register(Food, Ingredient, LogEntry)
class ItemAdmin(admin.ModelAdmin):
    pass

# Register your models here.
