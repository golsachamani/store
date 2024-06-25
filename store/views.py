from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from django.db.models import Q, F
def show_data(request):
    #product = Product.objects.filter(category__title__icontains= 'he')
    product = Product.objects.order_by('-inventory').values('name', 'inventory')
    return render(request, 'hello.html', {'products': list(product)})
