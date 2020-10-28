## COMMERCE

### Autores:
	Equipo desarrollo Curso Python - Django


### Ejecución del proyecto

1.- Activar el entorno virtual
	```pipenv shell```

2.- Ejecutar comando de runserver (Levantar el servicio web)
	```python manage.py runserver```

# FLUJO COMANDOS

1.- python manage.py makemigrations <nombre-app>    # Le indica al framework los cambios realizados en nuestro modelo de datos
2.- python manage.py migrate <nombre-app>       # Aplica los cambios definidos en el paso anterior

## Managers - Consultas ORM DJANGO

 - Product.objects.all() => Todos los objetos de producto.      # SELECT * from product;
 - Product.objects.filter(price__gt=Decimal("20.00")) => Devuelve todos los productos de precio mayor que USD 20.00
 - Product.objects.filter(price__gte=Decimal("20.00")) => Devuelve todos los productos de precio mayor o igual USD 20.00
 - Product.objects.filter(price__lt=Decimal("20.00")) => Devuelve todos los productos de precio menor que USD 20.00
 - Product.objects.filter(price__lte=Decimal("20.00")) => Devuelve todos los productos de precio menor o igual que USD 20.00
 - Product.objects.filter(name__icontains="Laptop") => Devuelve todos los productos llamados Laptop.
 - Product.objects.filter(category=2)	==> Devuelve todos los productos de la categoria con id=2.


## Managers - CREATE OR UPDATE ORM DJANGO
- Product.objects.create(name="A", price="10.4")
- Product.objects.get_or_create(name="A", price="10.4") => Devuelve la instancia del objecto creado
  * p = Product.objects.get_or_create(name="A", price="10.4")
- Product.objects.bulk_create([p1, p2, p3, p4])

- OrderItem.objects.filter(pk=1).update(price=25)
- o = OrderItem.objects.filter(pk=1).get_or_update.(price=25)


### Django sessions
- MIDDLEWARE (django.contrib.sessions.middleware.SessionMiddleware)
	request.session["cart"] = 'asdadasd1'
	del request.session['cart']