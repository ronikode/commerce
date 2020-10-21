"""
Urls de la aplicacion cart
"""
from carts.views import cart_add, cart_detail, cart_remove
from django.urls import path

app_name="carts"
urlpatterns = [
	path('', cart_detail, name="cart_detail"),
	path('agregar/<int:product_id>/', cart_add, name="cart_add"),
	path('borrar/<int:product_id>/', cart_remove, name="cart_remove")
]
