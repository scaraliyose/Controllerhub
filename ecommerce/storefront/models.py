"""Django data models for the ecommerce storefront application."""
from django.db import models
import datetime

# Create your models here.


class Customer(models.Model):
    """
        Customer table to store customer information
        - first_name
        - last_name
        - email
        - phone
        - password
    """
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=128, unique=True)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=32)

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name} - {self.email}"


class Product(models.Model):
    """
        Product table to store product information
        - name
        - description
        - price
        - stock
        - image
        - display_item
    """
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256, default="No description")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=5.00)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='uploads/products/', blank=True, null=True)
    display_item = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.stock} @ ${self.price}"

class Order(models.Model):
    """
        Order table to store order information
        - customer
        - address
        - date
        - status
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=256)
    date = models.DateTimeField(default=datetime.datetime.now)
    status = models.CharField(max_length=32, default="In Transit")

    def __str__(self) -> str:
        return f"Order {self.order_id} by {self.customer.first_name} {self.customer.last_name} - {self.status}"


class OrderItem(models.Model):
    """
        OrderItem (associative) table to store each item part of a given order
        - product
        - order
        - quantity
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"Order Item {self.order.order_id}: {self.product.name} x {self.quantity} = ${self.product.price * self.quantity}"


