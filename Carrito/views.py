from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from products.models import Product
from .models import Cart, Order
from django.contrib import messages


class Products(View):
    def get(self, request):
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'products/products_user.html', context)


class ViewCart(View):

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        cart = Cart.objects.get_or_create(user=user)[0]
        order = Order.objects.filter(cart=cart)
        context = {'cart': cart, 'order': order}
        return render(request, 'carts/CurrentCart.html', context)


class AddProduct(View):

    def get(self, request, pk):
        user = User.objects.get(id=request.user.id)
        cart = Cart.objects.get_or_create(user=user)[0]
        product = Product.objects.get(id=pk)

        Order.objects.create(cart=cart, product=product)

        product.stock -= 1
        product.save()

        cart.cost = cart.cost + product.price
        cart.save()

        return redirect('product_list')


class DeleteProductCart(View):

    def get(self, request, pk):
        user = User.objects.get(id=request.user.id)
        cart = Cart.objects.get(user=user)
        order = Order.objects.get(id=pk)
        product = order.product

        order.delete()

        product.stock += 1
        product.save()

        cart.cost = cart.cost - product.price
        cart.save()
        return redirect('view_cart')


class Purchase(View):

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        carts = Cart.objects.filter(user=user)

        for cart in carts:
            order = Order.objects.filter(cart=cart)
            order.delete()

        cart = Cart.objects.get(user=user)
        cart.cost = 0
        cart.save()

        messages.success(request, ('Purchase succesful!'))
        return redirect('view_cart')
