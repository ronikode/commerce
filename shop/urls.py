"""
Urls de la aplicacion shop
"""
from shop.views import product_list, ProductDetailView, product_catalogue, product_detail
from django.urls import path

app_name = "shop"

urlpatterns = [
    path("productos/", product_list, name="products"),
    path("productos/<int:pk>/", ProductDetailView.as_view(), name="products_detail"),
    # Catalogue
    path('<slug:category_slug>/', product_catalogue, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_info'),
]
