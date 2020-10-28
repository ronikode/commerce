"""Funciones/clases generales para el proyecto"""
from decimal import Decimal

import shortuuid
from datetime import datetime


def generate_unique_code():
    frame = datetime.now().strftime("%M%Y%H%M%S%f")  # month, year, hour, minutes, seconds, micro seconds
    cid = str(shortuuid.uuid()[:6]).upper()
    # "ABCA1233-1312313"
    return f"{cid}-{frame}"


class Item:

    def __init__(self, quantity, product, price, subtotal):
        self.quantity = quantity
        self.product = product
        self.price = price
        self.subtotal = subtotal


def map_cart_items(cart, form=None):
    """Funcion que devuelte listado items mapeado correctamente"""
    result = []
    for c in cart:
        if form:
            c[1]['update_quantity_form'] = \
                form(
                    initial={
                        'quantity': c[1].get('quantity'),
                        'override': True
                    }
                )
        result.append(
            Item(
                quantity=c[1].get("quantity"),
                product=c[1].get("product"),
                price=c[1].get("price"),
                subtotal=round(Decimal(c[1].get("price")) * Decimal(c[1].get("quantity")), 2)
            )
        )
    return result
