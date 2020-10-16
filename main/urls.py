"""
Urls de la aplicacion main
"""
from main.views import index, AboutView, ContactUsView	# Nombre de la vista
from django.urls import path


app_name="main"
urlpatterns = [
	path("", index, name="index"),
	
	# Acerca de
	path("acerca-de/", AboutView.as_view(), name="about"),
	path("contactanos/", ContactUsView.as_view(), name="contact"),

]
