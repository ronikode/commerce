
from shop.models import Product

class Cart:

	def __init__(self, request):	# Constructor
		"""Inicia un carrito"""
		self.session = request.session
		cart = self.session.get('cart_id')	# si no lo encuentra es un None
		if not cart:
			# Guardamos sesion de carrito vacio
			cart = self.session['cart_id'] = {}
		self.cart = cart
	
	def __iter__(self):
		"""
		Iterate los items del carrito y obtener productos
		"""

		product_ids = self.cart.keys() # -> Lista de la clave de dicho diccionario
		products = Product.objects.filter(id__in=list(product_ids))	# <atributo>__in=[2,3,4] ( debe ser una lista)

		cart_copy = self.cart.copy()	# Dict

		for product in products:
			cart_copy[str(product.id)]['product'] = product
		
		for item in cart_copy.items():
			item['price'] = item['price']
			item['subtotal'] = item['price'] * item['quantity']
	
	def __len__(self):
		"""Cantidad de items en el carrito"""
		# cont = 0
		# for item in self.cart.values():
		# 	cont += item.quantity
		return sum(item['quantity'] for item in self.cart.values())

	
	def add(self, product, qty=1, edit_qty=False):
		"""
		Agraga product al carrito y su cantidad
		"""
		product_id = str(product.id)

		if product_id not in self.cart:
			self.cart[product_id] = {
				"quantity": 0, "price": str(product.price)
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