
def global_quantity(req):
    cart = req.session.get('cart',{})
    quantity = 0
    if not cart:
        return {'cart_quantity':0}
    for val in cart.values():
        quantity += val

    return {'cart_quantity':quantity}