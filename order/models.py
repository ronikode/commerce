from django.db import models


class Order(models.Model):

	ORDER_STATUS = (
		(1, "Creada"),
		(2, "Procesada"),
		(3, "Enviada"),
		(4, "Pagada"),
		(5, "Completada"),
		(6, "Cancelada"),
	)

	ORDER_PAYMENT_MODE = (
		(1, "Efectivo"),
		(2, "Depostio/Transferencia"),
		(3, "Tarejeta de crédito")
	)

	code = models.CharField(max_length=100, unique=True, verbose_name="Código", help_text="Código único de la orden")
	date_created = models.DateTimeField(verbose_name="Fecha", auto_now=True, help_text="Fecha de emisión")	# Obtiene la fecha actual del servidor (equipo local)

	billing_name = models.CharField(max_length=200, verbose_name="Nombres factura", help_text="Nombres que se ingresan para la factura")
	billing_dni = models.CharField(max_length=20, verbose_name="No. Identificación", help_text="Numero de idenitifacion")
	billing_email = models.EmailField(verbose_name="Correo")
	billing_phone = models.CharField(max_length=20, null=True, blank=True)

	shipping_name = models.CharField(max_length=200, verbose_name="Nombres para entrega", help_text="Nombres que reciben el pedido de la orden")
	shipping_address = models.CharField(max_length=200, verbose_name="Dirección de entrega")
	shipping_phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Telefono para la entrega")

	payment_mode = models.IntegerField(
		default=1,
		choices=ORDER_PAYMENT_MODE, verbose_name="Forma de pago", help_text="modo de pago, Ej tarjeta de credito"
	)

	# Summary
	subtotal = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="SubTotal")
	base12 = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Base 12%")
	base0 = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Base 0%")
	iva = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="IVA")
	fee = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Fee entrega", default=0.0)
	total = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Total")

	# Orden - procesando, confirmada, entregada, pagada, completada o cancelada
	tracking_status = models.IntegerField(choices=ORDER_STATUS, default=1, help_text="Estado de seguimiento de la orden", verbose_name="Estado")


	class Meta:
		verbose_name = "Orden"
		verbose_name_plural = "Ordenes"
		db_table = "orden"
	
	def __str__(self):
		return self.code


