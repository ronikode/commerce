"""Context processor para setear el carrito actual en el contexto del request."""

from .cart import Cart


def cart(request):
    return {'cart': Cart(request)}
