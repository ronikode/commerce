""""""""

# Import standard
from decimal import Decimal

# Import django libraries
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Import custom apps
from coupons.models import Coupon
from shop.models import Product


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
    # Obtiene la fecha actual del servidor (equipo local)
    date_created = models.DateTimeField(verbose_name="Fecha", auto_now=True,
                                        help_text="Fecha de emisión")

    billing_name = models.CharField(max_length=200, verbose_name="Nombres factura",
                                    help_text="Nombres que se ingresan para la factura")
    billing_dni = models.CharField(max_length=20, verbose_name="No. Identificación",
                                   help_text="Numero de idenitifacion")
    billing_email = models.EmailField(verbose_name="Correo")
    billing_phone = models.CharField(max_length=20, null=True, blank=True)

    shipping_name = models.CharField(max_length=200, verbose_name="Nombres para entrega",
                                     help_text="Nombres que reciben el pedido de la orden")
    shipping_address = models.CharField(max_length=200, verbose_name="Dirección de entrega")
    shipping_phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Telefono para la entrega")

    payment_mode = models.IntegerField(
        default=1,
        choices=ORDER_PAYMENT_MODE, verbose_name="Forma de pago", help_text="modo de pago, Ej tarjeta de credito"
    )
    coupon = models.ForeignKey(
        Coupon,
        related_name='orders',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    discount = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    # Summary
    subtotal = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="SubTotal", default=0.0)
    base12 = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Base 12%", default=0.0)
    base0 = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Base 0%", default=0.0)
    iva = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="IVA", default=0.0)
    fee = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Fee entrega", default=0.0)
    discount_value = models.DecimalField(
        max_digits=9, decimal_places=2,
        verbose_name="Valor del descuento",
        default=0.0
    )
    total = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Total", default=0.0)

    # Orden - procesando, confirmada, entregada, pagada, completada o cancelada
    tracking_status = models.IntegerField(
        choices=ORDER_STATUS, default=1,
        help_text="Estado de seguimiento de la orden", verbose_name="Estado"
    )

    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Ordenes"
        db_table = "orden"

    def __str__(self):
        return self.code

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal(100))


class OrderItem(models.Model):
    # Relacion uno a muchos
    order = models.ForeignKey(
        Order, related_name="items",
        on_delete=models.CASCADE,
        verbose_name="Orden"
    )
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE, verbose_name="Producto")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Cantidad")

    def __str__(self):
        return f"[{self.order.code}] Item: {self.product}"

    def get_subtotal(self):
        return round(self.price * self.quantity, 2)
