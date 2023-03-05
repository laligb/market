from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

MY_ITEMS = [
    {'id': 1, 'name': 'bread', 'price': 0.5, 'quantity': 20},
    {'id': 2,'name': 'milk', 'price': 1.0, 'quantity': 10},
    {'id': 3,'name': 'wine', 'price': 10.0, 'quantity': 5},
]
def index(request):
    return render(request, 'frontend/build/index.html')

def productslistView(request):
    products = Product.objects.all()
    print(f"Product's items {products}")
    print(products.count())
    context = {
        'object_list': products,
    }
    template_name = "productslist.html"
    return render(request, template_name, context)



def productView(request, id):

    product = Product.objects.get(id=id)
    template_name = "product.html"
    context = {
        'object':product
    }
    return render(request, template_name, context)

def addProductView(request):
    template_name = "addProduct.html"
    form = ProductForm()

    if request.POST:
        form = ProductForm(request.POST)
        print('post test--------')

        if form.is_valid():
            form.save()
            return redirect('product-list')
        else:
            print(form.errors)

    context = {
        'form': form
    }
    return render(request,template_name,context)

def editProductView(request,id):

    template_name = 'editProduct.html'
    product = Product.objects.get(id=id)

    form = ProductForm(instance=product)
    if request.POST:
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-list')

    context = {
    'form':form,
        'product_id':product.id,
        'product': product,
    }
    return render(request,template_name,context)

def deleteProductView(request, id):
    product = Product.objects.get(id=id)
    if request.POST:
        product.delete()
    return redirect('product-list')


# Let's create view of serializer for API
# http://localhost:8000/api/products/
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'])
    def custom_action(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
