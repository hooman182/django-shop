from django.contrib import admin
from shop.models import Product, ProductModule, Image, File, Text, Video

# -------------------------------------------------------------

class AttributeCount(admin.SimpleListFilter):
    title = 'attribute count'
    parameter_name = 'attribute_count'

    def lookups(self, request, model_admin):
        return (
            ('more_5', 'more than 5 attributes'),
            ('lower_5', 'lower than 5 attributes'),
            ('0', 'no attributes'),
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(attributebase__isnull=True)
        elif self.value() == 'more_5':
            return queryset.annotate(attribute_count=Count('attributes')).filter(attribute_count__gte=5)
        elif self.value() == 'lower_5':
            return queryset.annotate(attribute_count=Count('attributes')).filter(attribute_count__lt=5)


class ProductModuleInline(admin.StackedInline):
    model = ProductModule
    extra = 2


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available', 'stock', 'discount', 'created', 'attribute_count']
    list_filter = ['available', 'updated', 'discount', AttributeCount]
    list_editable = ['price', 'available', 'discount']
    list_display_links = ['name']
    search_fields = ['name', 'description']
    list_per_page = 25
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductModuleInline]
    actions = ['make_available', 'make_unavailable']   

    def make_available(self, request, queryset):
        queryset.update(available=True)

    def make_unavailable(self, request, queryset):
        queryset.update(available=False)
    
    make_available.short_description = 'Mark selected products as available'
    make_unavailable.short_description = 'Mark selected products as un-available'
    
    def attribute_count(self, obj):
        return obj.attributes.count()

    

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    pass

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass
