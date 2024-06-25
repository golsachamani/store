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
# queryset_orderitem_products = OrderItem.objects.values('product__id').distinct()
#qeryset = Product.objects.filter(id__in=queryset_orderitem_products)
# .values()--> return dictionary 
# .value.lisdt()--> return as tuple in list
# .defer('x') --> return all field except x
# queryset = OrderItem.objects.select_related('order').all() --> bro to order ke forignkey khorde hame fieldasho harahe hame fieldae orderirem biar dar select_related yani oun model oun field dare forignkey khorde be modele dg (az OrderItem miresim be Order)
# queryset = Product.objects.prefetch_related('order_items').all() --> in dare az product mirese be orderitem yani boro product haye ro biar ke orderitem oun mosave x ----order_items -->related_name ke az orderitem forignkey khorde be product boro ounhaye payda kon forignkey khordan be product (az Orderitem miresim be product)
#aggregation ---> shamele count , max, min , ...... example ->queryset = Product.object.aggregate(count(id)) -> miad mire tedad prouduct mishmore barmigardune --> {'id__count': 100} mitunim chanta chiza baham be query bedim --> aggregate(count=count(id), max= Max(unit_price), ...)

# return product do not in orderitem ----> orderItem.objects.values('product_id').distict().count(
# ) ----> boro to orderitem product_i biar va uniqe kon vasam

#value ---> bekhaim ye add khasi seda bezanim

# F ---> field khasii bekham mosavi ya metenazer ham gharar bedim ---> id = F('inventory')

# aggregata
# expressinwraper ---> 
# Func --> queryset = Customer.objects.anntate(full_name=Func(F('first_name'),value(' '),F('last_name), function= 'CONCAT'))  ---> IN QUERY DARE mige boro to query ma fullname besaz va az function cancat estefade kon darvaghe concat miad ina beham vasl mikone

#annonate --> age bekhaim fieldi be modelmon azafe konin az in estefDE MIKONIN ALbate in field tu database ezafe nemishe
#queryset = OrderItem.objects.annotate(total_price = F('quantity')*F('unit_price)) --> fielde be esme total_price be query ma ezafe mishe

# group by --> queryset = Order.objects.annotate(count= Count(items)) items dar inja darvagh related_name order ba orderitem tu model