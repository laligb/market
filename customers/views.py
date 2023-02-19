from django.shortcuts import render

# Create your views here.

NAME = {'first_name': "Lali", 'last_name': "Bibilashvili"}

def customersView(request):
    template_name = "customers.html"
    context = NAME
    return render(request, template_name, context)
