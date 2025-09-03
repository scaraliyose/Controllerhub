from django.contrib import admin
from .models import Customer, Product, Order, OrderItem, Product, Review

# Register your models here.
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'average_rating', 'reviews_count')
    search_fields = ('name',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'rating', 'title', 'author_name', 'author_email', 'customer', 'created_at')
    list_filter = ('rating', 'created_at', 'product')
    search_fields = ('title', 'body', 'author_name', 'author_email')