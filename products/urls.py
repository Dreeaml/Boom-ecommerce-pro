from django.conf.urls import url
from .views import all_products, product_detail

urlpatterns = [
    url(r'^$', all_products,  name="products"),
    url(r'^(\d+)$', product_detail, name='product_detail'),
    #url(r'^<category>/$', all_products, name='all_products'),
    #path('<category>/', all_products, name='all_products'),
    #url(r'^(?P<category>[^\.]+)/$', all_products, name='all_products'),
]