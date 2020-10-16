from django import forms 
from django.core.mail import send_mail


class ContactForm(forms.Form):
	name = forms.CharField(label="Su nombre:", max_length=150, help_text="Ingrese sus nombres completos")
	message = forms.CharField(max_length=500, widget=forms.Textarea)

	def sending_email(self):
		"""
		Funcion que envia un correo electronico al usuario
		"""
		print("Enviando email al cliente")
		message = f"De: {self.cleaned_data['name']} \n {self.cleaned_data['message']}"
		send_mail(
			"Commerce",
			message,
			"info@commerce.com",
			["support@commerce.com"],
			fail_silently=False,
		)
		print("Despues del envio del correo")