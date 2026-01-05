from django.shortcuts import render
from .models import Category,Product


def category(req):
    cat = Category.objects.all()
    context = {
        'category':cat,
    }
    return render(req,'products/category.html',context)

def category_page(req,cat_id):
    category_products = Product.objects.filter(category_id=cat_id)
    single_category = Category.objects.get(pk=cat_id)
    print(single_category)
    print(category_products)
    context ={
        'category_products':category_products,
        'single_category':single_category,
    }
    return render(req,'products/category_page.html',context)


def product(req):
    products = Product.objects.all()
    context ={
        'products' : products
    }
    return render(req,'products/product.html',context)

