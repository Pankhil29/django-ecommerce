from .models import Category,Product

def category_list(req):
    category = Category.objects.all()
    return dict(category=category)

def product_list(req):
    product = Product.objects.all()
    return dict(product=product)