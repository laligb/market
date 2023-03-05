"""
URL configuration for market project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import render, redirect
from rest_framework import routers
from products import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet, 'products')

def index(request):
    return render(request, 'index.html')

def redirect_to_index(request):
    return redirect('index')

urlpatterns = [

    path('', index, name="index"),
    path('home/', redirect_to_index),
    path('home/', include('products.urls')),
    path('customers/', include('customers.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]
