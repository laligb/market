from django.urls import path
from .views import productslistView, productView, addProductView, editProductView, deleteProductView

from . import views

urlpatterns = [
    path('product-list',productslistView, name="product-list"),
    path('product/<int:id>/',productView, name="product"),
    path('add-product',addProductView,name="add-product"),
    path('product/<int:id>/add-product',addProductView,name="add-product"),
    path('edit-product/<int:id>',editProductView,name='edit-product'),
    path('delete-product/<int:id>', deleteProductView, name='delete-product'),

]
