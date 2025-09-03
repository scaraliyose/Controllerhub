from django.db import models
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
# from django.urls import clear_script_prefix
# from streamlit import status

# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=128, unique=True)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.last_name} {self.first_name} - {self.email}"


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256, default="No description")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=5.00)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='uploads/products/', blank=True, null=True)
    average_rating = models.FloatField(default=0.0)
    reviews_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.stock} @ ${self.price}"

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=256)
    date = models.DateTimeField(default=datetime.datetime.now)
    status = models.CharField(max_length=32, default="In Transit")

    def __str__(self):
        return f"Order {self.order_id} by {self.customer.first_name} {self.customer.last_name} - {self.status}"


class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Order Item {self.order.order_id}: {self.product.name} x {self.quantity} = ${self.product.price * self.quantity}"

class Review(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='reviews')
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, blank=True)
    author_name = models.CharField(max_length=64, blank=True)
    author_email = models.EmailField(max_length=128, blank=True)

    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        who = self.customer and f"{self.customer.first_name} {self.customer.last_name}" or self.author_name or "Anonymous"
        return f"{self.product.name} review by {who} ({self.rating}/5)"
