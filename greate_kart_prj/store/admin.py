from django.contrib import admin
from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'stock', 'price')
    list_display_links = ('product_name', 'category')
    prepopulated_fields = {'slug': ("product_name",)}


admin.site.register(Product, ProductAdmin)
