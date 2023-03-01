from django.urls import path
from .views import customersListView, customerView, addCustomerView, editCustomerView, deleteCustomerView

from . import views

urlpatterns = [    path('', customersListView, name='customers'),]


urlpatterns = [
    path('customer-list',customersListView, name="customer-list"),
    path('customer/<int:id>/',customerView, name="customer"),
    path('add-customer',addCustomerView,name="add-customer"),
    path('customer/<int:id>/add-customer',addCustomerView,name="add-customer"),
    path('edit-customer/<int:id>',editCustomerView,name='edit-customer'),
    path('delete-customer/<int:id>', deleteCustomerView, name='delete-customer'),
]
