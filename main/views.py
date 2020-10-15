from django.shortcuts import render


def index(request):
	print("controlador index")
	return render(request, "base.html", {})