"""Views controller about order."""
from decimal import Decimal

from django.core.mail import send_mail
from django.db import transaction
# Import django libraries
from django.shortcuts import render

# Import custom app
from carts.cart import Cart
from order.forms import OrderCreateForm
from order.models import OrderItem
from utils.general import map_cart_items, generate_unique_code


def create_order(request):
    cart = Cart(request)
    items = map_cart_items(cart)
    order_items = []
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            with transaction.atomic():  # Bloque controlado por transaction
                order = form.save(commit=False)  # Guarda una instancia previa al usar el commit=False de order.
                order.code = generate_unique_code()
                if cart.coupon:
                    order.coupon = cart.coupon
                    order.discount = cart.coupon.discount
                    order.subtotal = cart.get_total_subtotal()  # Suma Subtotales
                    order.base12 = order.subtotal  # Suma de items base12
                    order.iva = cart.get_total_subtotal() * Decimal(0.12)  # calcular impuesto
                    order.discount_value = round(Decimal(cart.get_discount()), 2)
                    order.total = round(cart.get_total_price_after_discount() + Decimal(order.fee))
                else:
                    order.subtotal = cart.get_total_subtotal()
                    order.base12 = order.subtotal
                    order.iva = round(cart.get_total_subtotal() * Decimal(0.12))  # TODO: Dinamico
                    order.total = round(order.subtotal + order.iva + Decimal(order.fee), 2)
                order.save()  # Insert en BD.

                for item in cart:
                    # order_items = [OrderItem1, OrderItem2, ....]
                    order_items.append(
                        OrderItem(
                            order=order,
                            product=item[1].get('product'),  # Instancia de objecto producto
                            price=item[1].get('price'),
                            quantity=item[1].get('quantity')
                        )
                    )
                    # OrderItem.objects.create(
                    # 	order=order,
                    # 	product=item[1].get('product'),	# Instancia de objecto producto
                    # 	price=item[1].get('price'),
                    # 	quantity=item[1].get('quantity')
                    # )
                OrderItem.objects.bulk_create(order_items)
                # Borrar los items asociados a ese carrito
                cart.clear()

                # Metodo de notificacion via correo del cliente
                send_mail(
                    "Commerce| Compra Exitosa",
                    f"Su orden con codigo {order.code} ha generada exitosamente.",
                    "info@commerce.com",
                    [order.billing_email],
                    fail_silently=False,
                )
                return render(request, "order/order_created.html", {'order': order})
    else:
        form = OrderCreateForm()
    return render(
        request, "order/order_form.html",
        {
            'cart': cart, 'form': form, 'items': items
        }
    )
