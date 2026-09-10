from django.contrib import admin
from .models import Category, Product, Customer

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity')
    list_filter = ('price',)
    search_fields = ('name', 'description')
    list_editable = ('price', 'quantity') # Позволяет менять цену прямо из списка!

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'address')
    search_fields = ('name', 'phone')