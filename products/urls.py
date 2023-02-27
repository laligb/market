from django.urls import path
from .views import productslistView, productView

from . import views

urlpatterns = [
    path('product-list',productslistView, name="product-list"),
    path('product/<int:id>/',productView, name="product")
]
