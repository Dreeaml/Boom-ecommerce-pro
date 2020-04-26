from django.conf.urls import url
from .views import view_cart, add_to_cart, remove_from_cart

urlpatterns = [
    url(r'^$', view_cart, name="view_cart"),
    url(r'^add/(?P<id>\d+)$', add_to_cart, name="add_to_cart"),
    #url(r'^add_one/(?P<id>\d+)$', add_one_to_cart, name="add_one_to_cart"),
    url(r'^remove/', remove_from_cart, name="remove_from_cart"),
]