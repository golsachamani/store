from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.db.models import Count
from django.utils.html import format_html
from django .urls import reverse
from django.utils.http import urlencode

from . models import *

class InventoryFillter(admin.SimpleListFilter):
    LESS_THAN_3 = '<3'
    BETWEN_3_AND_10 = '3<=10'
    GREATER_THAN_10= '>10'
    title = 'critical inventory status'
    parameter_name='inventory'
   
    def lookups(self, request, model_admin):
       
        return [
            (InventoryFillter.LESS_THAN_3, 'Medium'),
            (InventoryFillter.BETWEN_3_AND_10, 'High'),
            (InventoryFillter.GREATER_THAN_10, 'ok'),
        ]
    def queryset(self, request, queryset):
        if self.value()=='LESS_THAN_3':
            return queryset.filter(inventory__lt=3)
        
        if self.value()== 'BETWEN_3_AND_10':
            return queryset.filter(inventory__range=(3,10))
        
        if self.value()== 'grater_than_10':
            return queryset.filter(invventory__gt=10)

        


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name', 'category', 'unit_price','inventory','is_low', 'inventory_status','product_category', 'num_of_comments']
    list_editable =['unit_price']
    list_per_page=100
    list_select_related = ['category']
    list_filter =['datetime_created',InventoryFillter]
    search_fields =['name']
    prepopulated_fields ={'slug':['name']}
        
    
        
    
    def is_low(self, product):
        return product.inventory<10
    
    
    def get_queryset(self, request: HttpRequest):
        return super().get_queryset(request).prefetch_related('comments').annotate(count_comments=Count('comments'))
    
    @admin. display(ordering='count_comments',description='#comments')
    def num_of_comments(self, product):
        url =(
            reverse('admin:store_comment_changelist')+
            '?'+
            urlencode(
                {'product_id': product.id}
            )

        )
        # return product.count_comments
        return format_html('<a href ={}>{}</a>', url, product.comments_count)

    def inventory_status(self, product):
        if product.inventory<10:
            return 'low'
        if product.inventory>50:
            return 'high'
        return 'medium'
    @admin.display(ordering='category__title')
    def product_category(self, product):
        return product.category.title
 
admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(Address)
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields=['product', 'quantity', 'unite_price']
    extra = 0
    min_num =1
@admin.register(Order)
class OderAdmin(admin.ModelAdmin):
    list_display =['id', 'customer', 'status','datetime_created','num_of_item']
    list_editable=['status']
    ordering =['-datetime_created']
    inlines =[OrderItemInline]


    def get_queryset(self, request: HttpRequest):
        return super().get_queryset(request).prefetch_related('items').annotate(items_count=Count('items'))
    
    
    @admin.display(ordering='items_count',description='#items')
    def num_of_item(self,order):
       return order.items_count

@admin.register(Comment) 
class CommmentAdmin(admin.ModelAdmin):
    list_display=['name', 'product', 'status']  
    list_editable=['status']
    autocomplete_fields =['product']

admin.site.register(OrderItem)
admin.site.register(CartItem)

@admin.register(Customer)
class CustomAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name', 'email'] 
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields=['first_name__istartwith', 'last_name__istartwith']
class CartItemInline(admin.TabularInline):
    model =CartItem
    fields =['id', 'product','quantity']
    extra =0
    min_num =1

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','created_at' ]
    inlines = [CartItemInline]