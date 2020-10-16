from django.test import TestCase
from django.urls import reverse
from .forms import ContactForm

# TDD o Test Driven Development

class TestPage(TestCase):

	# Test page home
	def test_home_page_ok(self):
		response = self.client.get("/")	# Simula un llamado al navegador proyecto '/'
		self.assertEqual(response.status_code, 200)	# HTTP OK 200, CREATED 201, no found 404, internal error 500, not permissions 403
		self.assertTemplateUsed(response, 'main/home.html')

	def test_about_page_ok(self):
		response = self.client.get(reverse("main:about"))	# /acerca-de/
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'main/about.html')


class TestForm(TestCase):

	def test_valid_contact_form_sends_email(self):
		form = ContactForm(
			{
				"name": "Roberto", 
				"message": "Informacion de los productos"
			}
		)

		self.assertTrue(form.is_valid())

		form.sending_email()