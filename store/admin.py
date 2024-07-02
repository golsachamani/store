from django.contrib import admin

from . models import *
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name', 'category', 'unit_price','inventory','is_low', 'inventory_status']
    list_editable =['unit_price']
    list_per_page=100
    def is_low(self, product):
        return product.inventory<10
    
    def inventory_status(self, product):
        if product.inventory<10:
            return 'low'
        if product.inventory>50:
            return 'high'
        return 'medium'
admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(Customer)
admin.site.register(Address)
@admin.register(Order)
class OderAdmin(admin.ModelAdmin):
    list_display =['id', 'customer', 'status']
    list_editable=['status']

   


admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Comment)
    