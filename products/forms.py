
from django import forms
from .models import Product, Brand


class ProductCreate(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class BrandCreate(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
