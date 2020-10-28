from django import forms
from django.forms import fields
from .models import Order


class OrderCreateForm(forms.ModelForm):  # ModelForm

    class Meta:
        model = Order
        fields = [
            "billing_name",
            "billing_dni",
            "billing_email",
            "billing_phone",

            "shipping_name",
            "shipping_address",
            "shipping_phone",
            "payment_mode"
        ]
