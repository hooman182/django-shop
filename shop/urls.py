from django.urls import path
from shop import views


app_name = 'shop'

urlpatterns = [
    path('', views.prodcut_list, name='product_list'),
    path('<slug:category_slug>/', views.prodcut_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]