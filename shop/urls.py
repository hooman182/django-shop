from django.urls import path
from shop import views


app_name = 'shop'

urlpatterns = [
    path('', views.ProductsList.as_view(), name='product_list'),
    path('<str:category_slug>/', views.ProductsList.as_view(), name='product_list_by_category'),
    path('<int:id>/<str:slug>/', views.ProductsDetail.as_view(), name='product_detail'),
]