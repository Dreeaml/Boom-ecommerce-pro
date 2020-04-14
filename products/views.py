from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product
#from .forms import ProductsSearch

# Create your views here.
def all_products(request):
   # search_form  = ProductsSearch()
    products = Product.objects.all()
#------------------------------------------------------------
    # declare the min price and max price for the initial price filter bar
#    min_price=1
#    max_price=99
#
#   
#  # filter products based on min price
# if request.GET.get('min_price'):
#    products = products.filter(price__gte=request.GET.get('min_price'))
#   min_price=request.GET.get('min_price')
#    
#   # filter products based on max price
#  if request.GET.get('max_price'):
#     products = products.filter(price__lte=request.GET.get('max_price'))
#    max_price=request.GET.get('max_price')

    return render(request, "products.html", {"products": products })
#        { "search_products":search_form,
#        "min_price":min_price,
#        "max_price":max_price,}
       

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request,
                  'product_detail.html', {'product': product}) 
