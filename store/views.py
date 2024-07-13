from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.serializers import  CategorySerializer, ProductSerializer
from . models import *

@ api_view()
def product_list(request):
   product_queryset= Product.objects.select_related('category').all()
   serializer = ProductSerializer(product_queryset, many=True, context={'request':request})
   return Response(serializer.data)


@api_view()
def product_detail(request, pk):
   product = get_object_or_404(Product.objects.select_related('category').all(),pk=pk)
   # try:
   #    product = Product.objects.get(pk=id)
   # except Product.DoesNotExist:
   #    return Response(status=status.HTTP_404_NOT_FOUND)
   serializer = ProductSerializer(product, context={'request':request})
   return Response(serializer.data)


@ api_view()
def category_detail(request,pk):
   product =get_object_or_404(Category,pk=pk)
   selializer = CategorySerializer(product)
   return Response(selializer.data)