from django import forms

class CartAddProductForm(forms.Form):
	quantity = forms.IntegerField()
	