from django.shortcuts import render
from django.http import HttpResponse
from . models import *
def show_data(request):
    product = Product.objects.filter(category__title__icontains= 'he')
   
    return render(request, 'hello.html', {'products': list(product)})
# less than
# greater than
#greater than or equal to
# less than or equal to
# contain samthings -> products = Product.objects.filter(name__contain=Site) -> thos queryset return data that have Site word this is casesensitive if add i to contain ->icontain this is not casesensitive
# inventory__in=(1,4) -> in means instance that return 1 and 4 inventory in database
# queryset = Customer.objects.filter(barth_date__isnull=True) -> RETURN customer that their birth date is empyty or null