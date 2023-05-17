from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
