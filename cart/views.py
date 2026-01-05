from django.shortcuts import render,redirect
from products.models import Product
from django.shortcuts import get_object_or_404

# Create your views here.
def add_to_cart(req,pk):
    product = get_object_or_404(Product,pk=pk)

    cart = req.session.get('cart',{}) # if cart doesnot exist then return empty dict
    if str(pk) in cart:
        cart[str(pk)] += 1
    else:
        cart[str(pk)] = 1
        
    req.session['cart'] = cart
    req.session.modified = True
    
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    total_quantity = 0
    for pk, quantity in cart.items():
        product = Product.objects.get(id=pk)
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })
        total_quantity = quantity + total_quantity
    tax =total - (total * 10)/100
    

    context = {
        'cart_items': cart_items,
        'total': total,
        'tax' : tax
    }
    return render(request, 'products/cart.html', context)

def decrease_quantity(req,pk):
    cart = req.session.get('cart',{})
    
    if str(pk) in cart:
        if cart[str(pk)] > 1:
            cart[str(pk)] -= 1
        else:
            del cart[str(pk)]
    
    req.session['cart'] = cart
    req.session.modified = True
    
    return redirect('cart_detail')

def increase_quantity(req,pk):
    cart = req.session.get('cart',{})
    if str(pk) in cart:
        cart[str(pk)] += 1

    req.session['cart'] = cart
    req.session.modified = True
    return redirect('cart_detail')

def remove_from_cart(req,pk):
    cart = req.session.get('cart',{})
    
    if str(pk) in cart:
        del cart[str(pk)] 
    
    req.session['cart'] = cart
    req.session.modified = True

    return redirect('cart_detail')
