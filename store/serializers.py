from rest_framework import serializers
from decimal import Decimal
from . models import *

class CategorySerializer(serializers.Serializer):
     title = serializers.CharField(max_length=225)
     description= serializers.CharField(max_length=225)


class ProductSerializer(serializers.Serializer):
     id = serializers.IntegerField()
     name = serializers.CharField(max_length=225)
     unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
     inventory = serializers.IntegerField()
     unit_price_after_tax= serializers.SerializerMethodField()     
     # category = serializers.StringRelatedField()
     # category = CategorySerializer()
     category = serializers.HyperlinkedRelatedField(
          queryset = Category.objects.all(),
          view_name= 'category_detail'
     )
     
     def get_unit_price_after_tax(self, product):
          return round(product.unit_price * Decimal(1.09), 2)