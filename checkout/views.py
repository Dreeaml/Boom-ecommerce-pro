from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe


# Create your views here.
endpoint_secret = settings.endpoint_secret

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
            'amount': 1099,
            'currency' : 'sek',
            'quantity' : cart[id]['quantity']
        })
      
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        success_url=request.build_absolute_uri(reverse(checkout_success)),
        cancel_url=request.build_absolute_uri(reverse(checkout_cancelled)),
    )
    print(settings.STRIPE_PUBLISHABLE)  
    return render(request, 'checkout.html',
        {'session_id' : session.id,
        'public_key' : settings.STRIPE_PUBLISHABLE
    })

@login_required
def checkout_success(request):
    request.session['shopping_cart'] = {}
    return render(request, 'thankyou.html')

@login_required
def checkout_cancelled(request):
    all_products = Product.objects.all()
    min_price=1
    max_price=99
    
    return render(request, 'all_products.html', {
        'all_products':all_products,
        'min_price':min_price,
        'max_price':max_price
    })
  
  
@login_required   
@csrf_exempt
def payment_completed(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
        
    if event['type'] == 'checkout.session.completed':
        session =event['data']['object']
        
        handle_checkout_session(session)
    
    return HttpResponse(status=200)

def handle_checkout_session(session):
     print(session)