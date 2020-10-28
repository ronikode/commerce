"""Views/Controller app carts."""

# Import django libraries
from decimal import Decimal

from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from shop.models import Product
from .forms import CartAddProductForm
from coupons.forms import CouponApplyForm
from utils.general import Item
from .cart import Cart


# HTTP GET, POST, PUT, DELETE, PATCH

@require_POST  # es un decorador en django que solo permite envios de datos POST.
def cart_add(request, product_id):
    """"""
    cart = Cart(request)
    form = CartAddProductForm(request.POST)
    product = get_object_or_404(Product, id=product_id)  # Obtengo el objeto product
    if form.is_valid():  # True
        data = form.cleaned_data  # Dict {'quantity': 5}
        cart.add(
            qty=data.get("quantity"), product=product,
            edit_qty=data.get("override")
        )  # instancia objecto (producto)
    return redirect('carts:cart_detail')


@require_POST
def cart_remove(request, product_id):
    """"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product=product)
    return redirect("carts:cart_detail")


def cart_detail(request):
    cart = Cart(request=request)
    items = []
    # ('1', {"product": <>, "qty": <>, "price": <>})
    for c in cart:
        c[1]['update_quantity_form'] = \
            CartAddProductForm(
                initial={
                    'quantity': c[1].get('quantity'),
                    'override': True
                }
            )
        item = Item(
            quantity=c[1].get("quantity"),
            product=c[1].get("product"),
            price=c[1].get("price"),
            subtotal=round(Decimal(c[1].get("price")) * Decimal(c[1].get("quantity")), 2)
        )
        items.append(item)
    coupon_apply_form = CouponApplyForm()
    return render(request, "carts/detail.html", {'cart': cart, 'items': items, 'coupon_apply_form': coupon_apply_form})
