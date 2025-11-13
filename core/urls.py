from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('', include('shop.urls', namespace='shop')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

admin.site.site_title = "Admin panel"
admin.site.site_header = "ShopGo Admin Panel"
admin.site.index_title = "ShopGo"