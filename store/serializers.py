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
         fields =['id', 'name','body'] 


     def create(self, validated_data):
          product_id =self.context['product_pk']
          return Comment.objects.create(product_id=product_id,**validated_data)
     

class CartProductSerializer(serializers.ModelSerializer):
     class Meta:
          model =Product
          fields =['id', 'name', 'unit_price']

class UpdateCartItemSerializer(serializers.ModelSerializer):
     class Meta:
          model = CartItem
          fields = ['quantity']


class AddCartItemSerializer(serializers.ModelSerializer):
     class Meta:
          model =CartItem
          fields = ['id','product', 'quantity']
     def create(self, validated_data):
          cart_id = self.context['cart_pk']
          product = validated_data.get('product')
          quantity = validated_data.get('quantity')
          try:
               cart_item = CartItem.objects.filter(cart_id=cart_id,product_id=product.id)
               cart_item.quantity += quantity
               cart_item.save()
          except CartItem.DoesNotExist:
               CartItem.objects.create(cart_id = cart_id,**validated_data)
  
          self.instance = cart_item
          return cart_item
class CartItemSerializer(serializers.ModelSerializer):
     product = CartProductSerializer()
     item_total = serializers.SerializerMethodField()
     class Meta:
          model = CartItem
          fields =['id', 'product', 'quantity', 'item_total']
     def get_item_total(self, cart_items):
               return cart_items.quantity * cart_items.product.unit_price
     
class CartSerializer(serializers.ModelSerializer):
     total_price =serializers.SerializerMethodField()
     items = CartItemSerializer(many =True,read_only =True)
     # id = serializers.UUIDField(read_only =True)
     class Meta:
          model = Cart
          fields = ['id','created_at','items','total_price']
          read_only_fields =['id', ]
     def get_total_price(self, cart):
          return sum([item.quantity * item.product.unit_price for item in cart.items.all()])