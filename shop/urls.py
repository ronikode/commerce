"""
Urls de la aplicacion shop
"""
from shop.views import product_list, ProductDetailView 	#, ProductsListView
from django.urls import path


app_name="shop"

urlpatterns = [
	path("productos/", product_list, name="products"),
	# path("productos/catalogo/", ProductsListView.as_view(), name="products_list"),
	path("productos/<int:pk>/", ProductDetailView.as_view(), name="products_detail")
]
