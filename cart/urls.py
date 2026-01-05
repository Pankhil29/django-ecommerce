from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<int:pk>/',views.add_to_cart,name='add_to_cart'),
    path('cart_detail/',views.cart_detail,name='cart_detail'),
    path('decrease_quantity/<int:pk>/',views.decrease_quantity,name='decrease_quantity'),
    path('increase_quantity/<int:pk>/',views.increase_quantity,name='increase_quantity'),
    path('remove_from_cart/<int:pk>/',views.remove_from_cart,name='remove_from_cart'),
]   