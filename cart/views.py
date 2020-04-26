from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product
from django.contrib import messages


def view_cart(request):
    cart = request.session.get('shopping_cart', {})
    subtotal = 0
    total = 0
    
    # Calculate and display total price
    for idx,cart_item in cart.items():
        cart[idx]['subtotal'] = cart[idx]['price']*cart[idx]['quantity']
        total = total + cart[idx]['subtotal']
    
    return render(request, 'cart.html', {
        'shopping_cart':cart,
        'subtotal':subtotal,
        'total':total
    })
    

def add_to_cart(request, id):
    
    # get the object specified by the key 'shopping_cart', if not found, return an empty dictionary
    cart = request.session.get('shopping_cart', {})
    
    # Add the products specified by the products_id argument to cart
    product = get_object_or_404(Product, pk=id)
    quantity = int(request.POST['quantity'])
    if id not in cart:
        
        cart[id] = {
            'product_id':id,
            'name': product.name,
            'price': product.price,
            'quantity':quantity,
            #'image':'{{MEDIA_URL}}{{item.image}}'
            'image': '{{product.image}}'

        }
        
        # save the cart back to the session under the key 'shopping_cart'
        request.session['shopping_cart'] = cart
        
        messages.success(request, 'Product added to your cart!')
        return redirect('all_products')
    else:
        cart[id]['quantity']+=1
        request.session['shopping-cart'] = cart
        return redirect('all_products')
        
def remove_from_cart(request, id):
    cart=request.session.get('shopping_cart', {})
    
    # Remove the products specified by the products_id argument to cart
    if id in cart:
        del cart[id]
    
    request.session['shopping_cart'] = cart
    #return redirect('view_cart')
    return redirect('cart')


def back_to_shop(request, id):
    """return to products.html to keep shopping"""
    return redirect(reverse('all_products'))

    