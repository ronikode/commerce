from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, FormView

from .forms import ContactForm

# Vista basada en funcion
def index(request):
	return render(request, "main/home.html", {})

# Vista basada en clase TemplateView

class AboutView(TemplateView):
	template_name = "main/about.html"

class ContactUsView(FormView):
	template_name = "main/contact_form.html"
	form_class = ContactForm
	success_url = '/' # reverse("main:index")	# pagina de inicio # '/'

	def form_valid(self, form):
		print("formulario valido")
		form.sending_email()
		return super().form_valid(form=form)
	
	# def form_invalid(self, form: BaseForm) -> HttpResponse:


