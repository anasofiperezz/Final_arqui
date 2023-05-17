
from django.urls import path

from .views import *

urlpatterns = [
    path('', Products.as_view(), name='products'),
    path('products_user', ProductsUser.as_view(), name='products_user'),
    path('create_product', CreateProduct.as_view(), name='create_product'),
    path('create_brand', CreateBrand.as_view(), name='create_brand'),
    path('update/<int:id>', UpdateProduct.as_view(), name='update_product'),
    path('delete/<pk>', DeleteProduct.as_view(), name='delete_product'),
    path('delete/<pk>', DeleteBrand.as_view(), name='delete_brand'),
]
