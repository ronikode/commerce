"""Views/controller about shop."""

# Import django libraries
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

# Import custom apps
from carts.forms import CartAddProductForm
from .models import Product, Category  # Importando el modelo Product


# Vista basada en funcion
def product_list(request):
    print("Controlador de listado de productos")
    # API ORM DJANGO

    # SELECT * from product;
    products = Product.objects.all()  # Traer todos los registros de productos
    # print("cantidad: ", products.count())	# Recomendado
    # print(len(products))	# No se recomienda
    # Trae todos los registros de productos // select * from producto where stock = False;
    verified = Product.objects.filter(
        stock=False).exists()
    if verified:  # Boolean -> True o False
        print("Cuantos productos NO tengo disponibles: ",
              Product.objects.filter(stock=False).count())
    else:
        print("mis productos estan disponibles")
    context = {
        "products": products,
        "categories": Category.objects.filter(status=True)
    }
    return render(request, "shop/product_list.html", context)  # HTTPRESPONSE


# Vista basada en clase
class ProductDetailView(DetailView):  # CreateView, UpdateView, DeleteView, ListView
    """
    Vista o controlador que muestra la información de un objeto producto.
    """
    model = Product
    template_name = "shop/product_detail.html"
    context_object_name = "product"  # Atributo que indica el nombre de la variable que representa el objeto

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


def product_catalogue(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(
        request,
        "shop/product_list.html", {
            'category': category,
            'categories': categories,
            'products': products
        }
    )


def product_detail(request, id, slug):
    product = get_object_or_404(
        Product, id=id, slug=slug, stock=True
    )
    cart_product_form = CartAddProductForm()
    return render(
        request, "shop/product_detail.html",
        {
            'product': product,
            'cart_product_form': cart_product_form
        }
    )
