from django.shortcuts import render, redirect
from .models import Product

MY_ITEMS = [
    {'id': 1, 'name': 'bread', 'price': 0.5, 'quantity': 20},
    {'id': 2,'name': 'milk', 'price': 1.0, 'quantity': 10},
    {'id': 3,'name': 'wine', 'price': 10.0, 'quantity': 5},
]

def productslistView(request):
    products = Product.objects.all()
    print(f"Product's items {products}")
    print(products.count())
    context = {
        'object_list': products,
    }
    template_name = "productslist.html"
    return render(request, template_name, context)


# def productView(request, id):
#     if request.method == 'POST':
#         return redirect('productslist')
#     product = next((item for item in MY_ITEMS if item['id'] == id), None)
#     context = {'name': product['name'].upper(), 'price': product['price'], 'quantity': product['quantity']}
#     template_name = "product.html"
#     return render(request, template_name, context)

def productView(request, id):
    product = Product.objects.get(id=id)
    template_name = "product.html"
    context = {
        'object':product
    }
    return render(request, template_name, context)
