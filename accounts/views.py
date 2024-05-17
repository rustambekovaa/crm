from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders =Order.objects.count()
    deliverd = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders,'customers':customers,
               'total_customers':total_customers,
               'total_orders':total_orders,'deliverd':deliverd,
               'pending':pending
               }

    return render(request,'accounts/dashboard.html',context)

def products(request):
     products = Product.objects.all()
     return render(request,'accounts/products.html',{'products': products})

def customer(request,pk_test):
    customer = Customer.objects.get(id = pk_test)

    orders = customer.order_set.all()

    context = {'customer':customer,'orders':orders}

    return render(request,'accounts/customer.html',context)


def createOrder(request):

    context = {}
    return render(request,'accounts/order_form.html',context)


