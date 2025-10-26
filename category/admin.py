from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category

# -------------------------------------------------------

class CategoryAdmin(MPTTModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    mptt_level_indent = 20
    mptt_indent_field = 'name'
    
admin.site.register(Category, CategoryAdmin)