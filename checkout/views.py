from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe


# Create your views here.
endpoint_secret = settings.ENDPOINT_SECRET

@login_required()
def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET
    cart = request.session.get('shopping_cart', {})
    request.session['shopping_cart'] = {}
 
    line_items = []
    for id, product in cart.items():
        product = get_object_or_404(Product, pk=id)
        line_items.append({
            'name' : product.name,
            'amount': int(product.price * 100),
            'currency' : 'sek',
            'quantity' : cart[id]['quantity']
        })

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        success_url=request.build_absolute_uri(reverse(checkout_success)),
        cancel_url=request.build_absolute_uri(reverse(checkout_cancelled)),
    )
    print('shopping_cart')
    print(settings.STRIPE_PUBLISHABLE)  
    return render(request, 'checkout.html',
        {'session_id' : session.id,
        'public_key' : settings.STRIPE_PUBLISHABLE,
    })

@login_required
def checkout_success(request):
    request.session['shopping_cart'] = {}
    return render(request, 'thankyou.html')

@login_required
def checkout_cancelled(request):
    all_products = Product.objects.all()
    
    return render(request, 'all_products.html', {
        'all_products':all_products
    })
