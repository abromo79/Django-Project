from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
# Category: for product grouping (e.g., Electronics, Laptops)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# Product: your store items
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    stock = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="50"/>')
        return "No Image"

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name


# Customer: extends Django user
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.user.username


# Cart: one per customer
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart #{self.id} - {self.customer.user.username}"


# CartItem: multiple products per cart
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


# Order: placed after checkout
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    shipping_address = models.TextField()

    def __str__(self):
        return f"Order #{self.id} by {self.customer.user.username}"


# OrderItem: items inside the order
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def get_total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Order #{self.order.id})"
