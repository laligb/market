from django.urls import path
from .views import productslistView, productView

from . import views

urlpatterns = [
    path('productslist',productslistView, name="productslist"),
    path('productslist/<int:id>/',productslistView, name="productslist"),
    path('product/<int:id>/',productView, name="product")
]
