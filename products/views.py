from django.views.generic.edit import DeleteView
from django.shortcuts import redirect, render
from django.views import View
from .models import *
from .forms import ProductCreate, BrandCreate
from django.contrib.auth.decorators import login_required

# Create your views here.


class Products(View):
    def get(self, request):
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'products/products.html', context)


class ProductsUser(View):
    def get(self, request):
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'products/products_user.html', context)


class Brands(View):
    def get(self, request):
        products = Brand.objects.all()
        context = {'brands': brands}
        return render(request, 'products/products.html', context)


class CreateProduct(View):
    def get(self, request):
        form = ProductCreate()
        context = {'form': form}
        return render(request, 'products/form_producto.html', context)

    def post(self, request):
        form = ProductCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            print("FORM ERROR!")
            print(form.errors)
            context = {'form': form}
            return render(request, 'products/form_producto.html', context)


class CreateBrand(View):
    def get(self, request):
        form = BrandCreate(request.GET)
        context = {'form': form}
        return render(request, 'products/form_marca.html', context)

    def post(self, request):
        form = BrandCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            print("FORM ERROR!")
            print(form.errors)
            context = {'form': form}
            return render(request, 'products/form_marca.html', context)


class UpdateProduct(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        form = ProductCreate(instance=product)
        context = {'form': form}
        return render(request, 'products/update_form.html', context)

    def post(self, request, id):
        product = Product.objects.get(id=id)
        form = ProductCreate(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            print("FORM UPDATE ERROR!")
            print(form.errors)
            context = {'form': form}
            return render(request, 'products/update_form.html', context)


class DeleteProduct(DeleteView):
    model = Product
    success_url = "/products"
    template_name = "products/confirm_delete.html"


class DeleteBrand(DeleteView):
    model = Brand
    success_url = "/products"
    template_name = "products/confirm_delete.html"
