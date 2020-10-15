"""
Urls de la aplicacion main
"""
from main.views import index	# Nombre de la vista
from django.urls import path


app_name="main"
urlpatterns = [
	path("inicio/", index, name="index"),
]
