from django.contrib import admin

from .models import OrderItem, Order  # Importa los modelos de la aplicacion (order)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['billing_dni', 'code', "billing_name"]
    list_filter = ['tracking_status']
    inlines = [OrderItemInline]
