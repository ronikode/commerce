from shop.models import Category
from django.contrib import admin

# Import models app
from .models import Category, Product, ProductImage

# Create Read Update Delete (CRUD)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'code')	# Campos del modelo que se ven en el listado
	fields = ('name', 'description', 'code')	# Campos a mostrar en el formulario del modelo
	search_fields = ("name", "code",)

class ProductAdmin(admin.ModelAdmin):
	list_display = ('sku','name', 'price', 'category', "stock")	# Campos del modelo que se ven en el listado
	fields = ('sku', 'name', 'category', 'price', 'stock', 'description')	# Campos a mostrar en el formulario del modelo
	search_fields = ("name", "sku",)
	list_editable = ["stock", ]	# Lista los campos editables directamente
	raw_id_fields = ["category",]



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductImage)