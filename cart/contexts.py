from django.shortcuts import get_object_or_404
from products.models import Product

'''def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart = request.session.get('cart', {'product_list': []})
    
    product_count = len(cart['product_list'])
    print("cart", cart)
    
    return {'product_count': product_count}'''

def cart_contents(request):
    cart = request.session.get("shopping_cart", {})
    print(cart)

    product_count = len(cart)
    
    return {
        'shopping_cart':cart,
        'product_count': product_count
    }