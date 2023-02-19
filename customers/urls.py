from django.urls import path
from .views import customersView

from . import views

urlpatterns = [    path('', customersView, name='customers'),]
