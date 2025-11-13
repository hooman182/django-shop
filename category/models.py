from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
# -------------------------------------------------------

class Category(MPTTModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    is_active = models.BooleanField(default=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']
        
    class Meta:
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def __str__(self) -> str:
        return self.name
    
    def category_products(self):
        
        from shop.models import Product
        return Product.objects.filter(category=self).count()
