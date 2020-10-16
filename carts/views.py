from carts.forms import CartAddProductForm
from django.shortcuts import render

from .cart import Cart


def cart_add(request, product_id):
	""""""
	cart = Cart(request)
	form = CartAddProductForm()
	# TODO: por avanzar

	return render(request, "", {})