from django.contrib import admin

# Register your models here.
from .models import CustomerModel
# Register your models here.
@admin.register(CustomerModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'is_active', 'email')
