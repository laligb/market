from django.shortcuts import render, redirect
from .models import CustomerModel
from .forms import CustomerForm

# Create your views here.

NAME = {'first_name': "Lali", 'last_name': "Bibilashvili"}

def customersListView(request):
    customers = CustomerModel.objects.all()
    template_name = "customerslist.html"
    # context = NAME
    context = {
        'customer_list': customers,
    }
    return render(request, template_name, context)


def customerView(request, id):
    customer = CustomerModel.objects.get(id=id)
    template_name = "customer.html"
    context = {
        'customer':customer
    }
    return render(request, template_name, context)

def addCustomerView(request):
    template_name = "addCustomer.html"
    form = CustomerForm()

    if request.POST:
        form = CustomerForm(request.POST)
        print('post test--------')

        if form.is_valid():
            form.save()
            return redirect('customer-list')
        else:
            print(form.errors)

    context = {
        'form': form
    }
    return render(request,template_name,context)

def editCustomerView(request,id):

    template_name = 'editCustomer.html'
    customer = CustomerModel.objects.get(id=id)

    form = CustomerForm(instance=customer)
    if request.POST:
        form = CustomerForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer-list')

    context = {
    'form':form,
        'customer_id':customer.id,
        'customer': customer,
    }
    return render(request,template_name,context)

def deleteCustomerView(request, id):
    customer = CustomerModel.objects.get(id=id)
    if request.POST:
        customer.delete()
    return redirect('customer-list')
