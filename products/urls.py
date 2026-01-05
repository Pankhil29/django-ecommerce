from django.urls import path
from . import views


urlpatterns = [
    path('',views.category,name='category'),
    path('category_page/<int:cat_id>/',views.category_page,name='category_page'),
    path('product/',views.product,name='product'),
        
]