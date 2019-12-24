from django.contrib import admin
from .models import Food, Ingredient

@admin.register(Food, Ingredient)
class ItemAdmin(admin.ModelAdmin):
    pass

# Register your models here.
