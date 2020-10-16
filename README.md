## COMMERCE

### Autores:
	Equipo desarrollo Curso Python - Django


### Ejecución del proyecto

1.- Activar el entorno virtual
	```pipenv shell```

2.- Ejecutar comando de runserver (Levantar el servicio web)
	```python manage.py runserver```



## Managers - Consultas ORM DJANGO

 - Product.objects.all() => Todos los objetos de producto.
 - Product.objects.filter(price__gt=Decimal("20.00")) => Devuelve todos los productos de precio mayor que USD 20.00
 - Product.objects.filter(price__gte=Decimal("20.00")) => Devuelve todos los productos de precio mayor o igual USD 20.00
 - Product.objects.filter(price__lt=Decimal("20.00")) => Devuelve todos los productos de precio menor que USD 20.00
 - Product.objects.filter(price__lte=Decimal("20.00")) => Devuelve todos los productos de precio menor o igual que USD 20.00
 - Product.objects.filter(name__icontains="Laptop") => Devuelve todos los productos llamados Laptop.
 - Product.objects.filter(category=2)	==> Devuelve todos los productos de la categoria con id=2.

### Django sessions
- MIDDLEWARE (django.contrib.sessions.middleware.SessionMiddleware)

	request.session["cart"] = 'asdadasd1'

	del request.session['cart']

