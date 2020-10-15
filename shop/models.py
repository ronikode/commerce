from django.db import models


class Category(models.Model):
	"""
	Categoria de producto	
	"""
	name = models.CharField(verbose_name="Nombre", help_text="Nombre de la categoría", max_length=200)
	code = models.CharField(verbose_name="Código", help_text="Código representativo de la categoría", max_length=20)
	description = models.TextField(blank=True, null=True, verbose_name="Descripción", help_text="Descripción categoría")
	status = models.BooleanField(default=True, verbose_name="Estado", help_text="Muestra categorias activas")

	def __str__(self): # toString
		return f"[{self.code}] {self.name}"
	
	class Meta:
		verbose_name = "Categoría"	# singular
		verbose_name_plural = "Categorías"	# categorías
		db_table = "categoria"	# si no uso el db_table => <nombre_app>_category o shop_category


class Product(models.Model):
	"""
	Clase producto
	"""
	sku = models.CharField(max_length=50, unique=True, verbose_name="SKU", help_text="Codigo control inventario")
	name = models.CharField(max_length=150, verbose_name="Nombre", help_text="Nombre producto")
	price = models.DecimalField(verbose_name="Precio venta", decimal_places=2, max_digits=8, help_text="Precio de venta en USD.")
	category = models.ForeignKey(
		Category, verbose_name="Categoría", 
		help_text="Categoría del producto", 
		on_delete=models.SET_NULL, null=True, blank=True
	)
	stock = models.BooleanField(default=True, verbose_name="Disponibilidad", help_text="Existencia del producto")
	description = models.TextField(blank=True, default='', verbose_name="Descripción", help_text="Descripción del producto")

	class Meta:
		verbose_name = "Producto"
		verbose_name_plural = "Productos"
		db_table = "producto"
	
	def __str__(self):
		return f"{self.name}"


class ProductImage(models.Model):
	"""
	"""
	product = models.ForeignKey(
		Product, on_delete=models.CASCADE, 
		verbose_name="Producto", related_name="images"
	)
	photo = models.ImageField(upload_to="product-images")	# Directorio donde se almacena las imagenes
	thumbnail = models.ImageField(upload_to="product-thumbnails" , null=True, blank=True)	# Es opcional en el administrador. 

	class Meta:
		verbose_name = "Imagen producto"
		verbose_name_plural = "Imagenes producto"
		db_table = "producto_image"
	
	def __str__(self):
		return f"Foto de {self.product}"