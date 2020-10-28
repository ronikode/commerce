""""""""
# Import libraries standard
from decimal import Decimal

# Import custom apps
from shop.models import Product
from coupons.models import Coupon


# cart = Cart(request)
# cart.coupon

class Cart:

    def __init__(self, request):  # Constructor
        """Inicia un carrito"""
        self.session = request.session
        cart = self.session.get('cart_id')  # si no lo encuentra es un None
        # store current applied coupon
        self.coupon_id = self.session.get('coupon_id')
        if not cart:
            # Guardamos sesion de carrito vacio
            cart = self.session['cart_id'] = {}
        self.cart = cart

    @property
    def coupon(self):
        if self.coupon_id:
            try:
                return Coupon.objects.get(id=self.coupon_id)    # SELECT * FROM coupon where id=coupon_id;
            except Coupon.DoesNotExist:
                pass
        return None

    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount / Decimal(100)) * self.get_total_subtotal()
        return Decimal(0)

    def get_total_price_after_discount(self):
        return self.get_total_subtotal() - self.get_discount()

    def __iter__(self):
        """
        Iterate los items del carrito y obtener productos
        """
        product_ids = self.cart.keys()  # -> Lista de la clave de dicho diccionario
        products = Product.objects.filter(id__in=list(product_ids))  # <atributo>__in=[2,3,4] ( debe ser una lista)
        cart_copy = self.cart.copy()  # Dict
        for product in products:
            cart_copy[str(product.id)]['product'] = product

        for item in cart_copy.items():
            price = item[1].get('price')
            qty = item[1].get('quantity')
            item[1]['price'] = price
            item[1]['subtotal'] = price * qty
            yield item

    def __len__(self):
        """Cantidad de items en el carrito"""
        # cont = 0
        # for item in self.cart.values():
        # 	cont += item.quantity
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, qty=1, edit_qty=False):
        """
        Agraga producto al carrito y su cantidad
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": 0,
                "price": str(product.price)
            }

        if edit_qty:
            self.cart[product_id]['quantity'] = qty
        else:
            self.cart[product_id]['quantity'] += qty

        self.save()

    def save(self):
        """

        """
        # self.session -> {}
        self.session.modified = True

    def remove(self, product):
        """
        Elimina el product del carrito
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_subtotal(self):
        return sum(Decimal(item.get("price")) * item.get('quantity') for item in self.cart.values())

    def clear(self):
        # Eliminia el carrito (objecto) de la sesion
        del self.session['cart_id']
        del self.session['coupon_id']
        self.save()
