from django.shortcuts import get_object_or_404
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter,SearchFilter 
from store.serializers import  CategorySerializer, CommentSerializer, ProductSerializer
from . models import *

class ProductViewSet(ModelViewSet):
   serializer_class =ProductSerializer
   queryset =Product.objects.all()
   filter_backends =[DjangoFilterBackend,OrderingFilter,SearchFilter]
   filterset_fields =['category_id']
   ordering_fields =['name', 'unit_price', 'inventory']
   search_fields =['name']
   # def get_queryset(self):
   #    queryset= Product.objects.all()
   #    category_id_parameters=self.request.query_params.get('category_id')
   #    if category_id_parameters is not None:
   #       queryset = queryset.filter(category_id=category_id_parameters)

      # return super().get_queryset()
   # def get_serializer_class(self):
   #     return ProductSerializer
   # def get_queryset(self):
   #     return Product.objects.select_related('category').all()
   def get_serializer_context(self):
       return {'request':self.request}


   def destroy(self,request,pk):
         product = get_object_or_404(Product.objects.select_related('category').all(),pk=pk)
         if product.order_items.count()>0:
            return Response({'error':'not allow'},status =status.HTTP_405_METHOD_NOT_ALLOWED, )
         product.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
   
        

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset =Category.objects.prefetch_related('products').all()

    def delete(self,request,pk):
         category =get_object_or_404(Category.objects.prefetch_related('products').all(),pk=pk)
         category.delete()
         if category.products.count()>0:
            return Response({'error':'not allow'},status =status.HTTP_405_METHOD_NOT_ALLOWED, )
         return Response(status=status.HTTP_204_NO_CONTENT)   


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        product_pk = self.kwargs['product_pk']
        return  Comment.objects.filter(product_id=product_pk).all()
    
    def get_serializer_context(self):
        return {'product_pk':self.kwargs['product_pk']}




















   #  def get(self,request):
   #       categories_queryset = Category.objects.prefetch_related('products').all()
   #       serializer = CategorySerializer(categories_queryset, many=True)
   #       return Response(serializer.data)
   #  def post(self, request):
   #      serializer = CategorySerializer(data=request.data)
   #      serializer.is_valid(raise_exception=True)
   #      serializer.validated_data
   #      serializer.save()
   #      return Response(serializer.data, status=status.HTTP_201_CREATED) 
      #  def get(self,request,pk):
   #    category =get_object_or_404(Category.objects.prefetch_related('products').all(),pk=pk)
   #    selializer = CategorySerializer(category)
   #    return Response(selializer.data)
   #  def put(self,request,pk):
   #       category =get_object_or_404(Category.objects.prefetch_related('products').all(),pk=pk)
   #       serializer = CategorySerializer(category,data=request.data)
   #       serializer.is_valid(raise_exception=True)
   #       serializer.save()
   #       return Response(serializer.data)  

     #  def get(self,request,pk):
   #       product = get_object_or_404(Product.objects.select_related('category').all(),pk=pk)
   #       serializer = ProductSerializer(product, context={'request':request})
   #       return Response(serializer.data)  
   #  def put(self, request,pk):
   #        product = get_object_or_404(Product.objects.select_related('category').all(),pk=pk)
   #        serializer = ProductSerializer(product,data=request.data)
   #        serializer.is_valid(raise_exception=True)
   #        serializer.save()
   #        return Response(serializer.data)