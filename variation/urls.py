from django.urls import path
from .views import add_product_view, product_list_view, add_category_view, category_list_view

urlpatterns = [
    path('', add_product_view, name='add_product'),
    path('product-list/', product_list_view, name='product_list'),
    path('add-category/', add_category_view, name='add_category'),
    path('category-list/', category_list_view, name='category_list'),
]
