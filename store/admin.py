from django.contrib import admin
from store.models import Product2, Order, ShippingAddress, Category

# Register your models here.

@admin.register(Product2)
class Product2Admin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'image', 'stock']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'ordered_at', 'complete', 'transaction_id']


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'order', 'address', 'city', 'zip_code', 'country']

# admin.site.register(Product2)
# admin.site.register(Category)
# admin.site.register(Order)
# # admin.site.register(OrderItem)
# admin.site.register(ShippingAddress)