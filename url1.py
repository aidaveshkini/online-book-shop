from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account_module.urls', namespace='account')),
    path('products/', include('product_module.urls', namespace='product')),
    path('order/', include('order_module.urls', namespace='order'))
]
