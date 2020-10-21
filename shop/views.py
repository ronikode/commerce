from carts.forms import CartAddProductForm
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Product, Category	 # Importando el modelo Product


# Vista basada en funcion
def product_list(request):
	print("Controlador de listado de productos")
	# API ORM DJANGO
	
	# SELECT * from product;
	products = Product.objects.all()	# Traer todos los registros de productos
	# print("cantidad: ", products.count())	# Recomendado
	# print(len(products))	# No se recomienda

	verified = Product.objects.filter(stock=False).exists()	# Traer todos los registros de productos // select * from producto where stock = False;
	if verified:	# Boolean -> True o False
		print("Cuantos productos NO tengo disponibles: ", Product.objects.filter(stock=False).count())
	else:
		print("mis productos estan disponibles")
	context = {
		"products": products,
		"categories": Category.objects.filter(status=True)
	}
	return render(request, "shop/product_list.html", context)	# HTTPRESPONSE


# Vista basada en clase
class ProductDetailView(DetailView):	# CreateView, UpdateView, DeleteView, ListView
	"""
	Vista o controlador que muestra la información de un objeto producto.
	"""
	model = Product
	template_name = "shop/product_detail.html"
	context_object_name = "product"		# Atributo que indica el nombre de la variable que representa el objeto

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cart_product_form = CartAddProductForm()

		context["cart_product_form"] = cart_product_form
		context["title"] = "Detalle del producto en la vista de clase"
		return context


class ProductsListView(ListView):
	"""
	
	"""
	model = Product
	template_name = "shop/product_list.html"
	queryset = Product.objects.all()
	context_object_name = "products"