"""Cart Forms."""

# Import django libraries
from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]  # [1 - 10]


class CartAddProductForm(forms.Form):
    # Convierte el input en entero
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES, coerce=int
    )
    # Esto indica si la cantidad agrega alguna cantidad existente en el carrito,
    # False si la cantidad existente ha sido sobrescrita
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )
