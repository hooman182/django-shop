from django.contrib import admin
from shop.models import Product

# -------------------------------------------------------

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available', 'slug', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'price']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    
admin.site.register(Product, ProductAdmin)
