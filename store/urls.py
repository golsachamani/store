from django.urls import path,include
from rest_framework_nested import routers
from .views import *

# urlpatterns = [
#    path('products/',ProductList.as_view(),name='product_list'),
#    path('products/<int:pk>/',ProductDetail.as_view(),name='product_detail'),
#    path('categories/',CategoryList.as_view(), name='category_list'),
#    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
# ]
router = routers.DefaultRouter()
router.register('products',ProductViewSet,basename='product')
router.register('categories', CategoryViewSet,basename='category')
router.register('carts', CartViewSet, basename='cart')
product_router = routers.NestedDefaultRouter(router,'products',lookup='product')
product_router.register('comments', CommentViewSet, basename='product_comment')

cart_item_router = routers.NestedDefaultRouter(router,'carts', lookup = 'cart')
cart_item_router.register('items', CartItemViewSet,basename='cart_cartitems')
urlpatterns=router.urls + product_router.urls + cart_item_router.urls