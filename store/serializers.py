from rest_framework import serializers
from decimal import Decimal
from . models import *
from django.utils.text import slugify
class CategorySerializer(serializers.ModelSerializer):
     num_of_products = serializers.SerializerMethodField() 
     class Meta:
          model = Category
          fields =['id', 'title','description','num_of_products'] 

     def get_num_of_products(self,category):
          return category.products.count()

class ProductSerializer(serializers.ModelSerializer):
     title = serializers.CharField(max_length=225,source = 'name')
     price = serializers.DecimalField(max_digits=6, decimal_places=2,source='unit_price')
     unit_price_after_tax= serializers.SerializerMethodField()     
     # category = serializers.StringRelatedField()
     category = CategorySerializer()
     # category = serializers.HyperlinkedRelatedField(
     #      queryset = Category.objects.all(),
     #      view_name= 'category_detail'
     # )
     class Meta:
          model = Product
          fields =['id', 'title','price','inventory','category','unit_price_after_tax','slug']
     def get_unit_price_after_tax(self, product):
          return round(product.unit_price * Decimal(1.09), 2)
     
     def create(self, validated_data):
          product =Product(**validated_data)
          product.slug = slugify(product.name)
class CommentSerializer(serializers.ModelSerializer):
     class Meta:
         model = Comment
         fields =['id', 'name', 'product','body'] 