# Import django libraries
from django.shortcuts import render
from django.views.generic import TemplateView, FormView

# Import custom apps
from shop.models import Product
from .forms import ContactForm


# Vista basada en funcion
def index(request):
    products = Product.objects.all()  # SELECT * FROM product;
    return render(request, "main/home.html", {"products": products})


# Vista basada en clase TemplateView

class AboutView(TemplateView):
    template_name = "main/about.html"


class ContactUsView(FormView):
    template_name = "main/contact_form.html"
    form_class = ContactForm
    success_url = '/'  # reverse("main:index")	# pagina de inicio # '/'

    def form_valid(self, form):
        print("formulario valido")
        form.sending_email()
        return super().form_valid(form=form)

    # def form_invalid(self, form: BaseForm) -> HttpResponse:
