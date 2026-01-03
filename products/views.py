from django.shortcuts import render
from .models import Category,Product


def category(req):
    cat = Category.objects.all()
    context = {
        'category':cat,
    }
    return render(req,'products/category.html',context)


def product(req):
    products = Product.objects.all()
    context ={
        'products' : products
    }
    return render(req,'products/product.html',context)