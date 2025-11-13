from django.shortcuts import get_object_or_404
from cart.forms import CartAddProductForm
from shop.models import Product
from category.models import Category
from django.views.generic import ListView, DetailView


class ProductsList(ListView):
    model = Product
    template_name = 'shop/product/list.html'
    paginate_by = 12
    context_object_name = 'products'
    
    def get_queryset(self):
        queryset = Product.objects.filter(available=True)
        self.category = None
        
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=self.category)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['category'] = self.category
        context['cart_form'] = CartAddProductForm()
        return context
    
class ProductsDetail(DetailView):
    model = Product
    template_name = 'shop/product/detail.html'
    context_object_name = 'product'
    
    def get_object(self, queryset=None):
        return get_object_or_404(Product, id=self.kwargs['id'], slug=self.kwargs['slug'], available=True)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_form'] = CartAddProductForm()
        return context
