from .models import Category

def category_list(req):
    category = Category.objects.all()
    return dict(category=category)