from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from django.db.models import Q, F
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
# queryset = Product.objects.filter(inventory__gt =5).filter(name__icontains='he').filter(create_time__year=2021) ---> this queryset show we can do many filter beside each other and we can show filter(inventory__gt =5 ,name__icontains='he', create_time__year=2021 )
#queryset_jean = Customer.objects.filter(first_name__icontains='jean)
# queryset = Order.objects.filter(customer__in=queryset_john)
# Q object
# F object --> queryset = OrderItem.objects.filter(product__id= F('quantity')) --> this query says product id equall to quantity return this quary 
# indexing --> Product.objects.all()[:10] return first 10 number