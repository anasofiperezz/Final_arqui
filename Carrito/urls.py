
from django.urls import path

from .views import *

urlpatterns = [
    path('/cart', ViewCart.as_view(), name='view_cart'),
    path('', Products.as_view(), name='product_list'),
    path('add/<pk>', AddProduct.as_view(), name='add_product'),
    path('delete/<pk>', DeleteProductCart.as_view(), name='delete_productcart'),
    path('purchase', Purchase.as_view(), name='purchase'),
]
