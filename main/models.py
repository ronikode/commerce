from django.db import models

# Create your models here.
class BaseShop(models.Model):

	tax_shipping = models.DecimalField(max_digits=9, decimal_places=2, help_text="Fee de entrega")
	pvp_iva = models.BooleanField(default=False, help_text="Precio venta incluye iva")

	class Meta:
		verbose_name = "Configuracion Tienda"
		db_table = "base_shop"