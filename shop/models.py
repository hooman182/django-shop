from django.db import models
from django.urls import reverse
from category.models import Category

# -------------------------------------------------------
        
class ProductAvailableManager(models.Manager):
    
    use_for_related_fields = True 
    
    def get_queryset(self):
        return super().get_queryset().filter(available=True)

class ProductHasDiscountManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(available=True)
        
class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, allow_unicode=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=3)
    cover = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=0)
    discount = models.PositiveIntegerField(default=0)
    
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    
    # availabled = ProductAvailableManager()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name', 'price']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['-created']),
        ]
    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
    
    def __str__(self):
        return self.name
    
    @property
    def has_attribute(self):
        return self.attributes.exists()
    
    @property
    def has_discount(self):
        return self.discount > 0
    
    @property
    def get_available_products(self):
        return self.available
    
    
class ProductModule(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes')
    
    title = models.CharField(max_length=255, blank=True, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title} - {self.product}'
        
class AttributeBase(models.Model):
    product_module = models.ForeignKey(ProductModule, on_delete=models.CASCADE, related_name='%(class)s_related')
    
    class Meta:
        abstract = True
            
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
class Image(AttributeBase):
    image = models.ImageField(upload_to='products/images/%Y/%m/%d', blank=True, verbose_name='تصویر')
    
    @property
    def model_name(self):
        return "image"
    
class File(AttributeBase):
    file = models.FileField(upload_to='products/files/%Y/%m/%d', blank=True, verbose_name='فایل')
    
    @property
    def model_name(self):
        return "file"
        
class Video(AttributeBase):
    video = models.FileField(upload_to='products/videos/%Y/%m/%d', blank=True, verbose_name='ویدیو')
    
    @property
    def model_name(self):
        return "video"

class Text(AttributeBase):
    text = models.TextField(blank=True, verbose_name='متن')
    
    @property
    def model_name(self):
        return "text"


class ProductGroup(models.Model):
    product_module = models.ForeignKey(ProductModule, on_delete=models.CASCADE, related_name='group')
    
    # title   = models.CharField(max_length=255)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    
class ProductGroupOption(models.Model):
    product_group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE, related_name='options')
   