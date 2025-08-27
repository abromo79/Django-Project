from django.contrib import admin
from .models import Category, Product, Customer, Cart, CartItem, Order, OrderItem


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'available', 'image_tag')
    readonly_fields = ('image_tag',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address')


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'created_at')


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'get_total_price')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'ordered_at', 'is_paid')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'get_total_price')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
