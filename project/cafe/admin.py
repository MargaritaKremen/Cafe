from django.contrib import admin
from .models import Category, Ingredient, Item, Order

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Order)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'image')
