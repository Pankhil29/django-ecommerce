from django.urls import path
from . import views


urlpatterns = [
   
    path('category_page/<int:cat_id>/',views.category_page,name='category_page'),
    path('product/',views.product,name='product'),

    # product details
    path('product_details/<int:pk>/',views.product_details,name='product_details'),
    # path('category/product/',views,name='product_details'),
        
]