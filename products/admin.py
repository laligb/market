from django.contrib import admin
# Register your models here.
from .models import Product, Order
from .models import Customer

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','quantity')

@admin.register(Customer)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'status')

@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantity', 'customer_id', 'product_id')
