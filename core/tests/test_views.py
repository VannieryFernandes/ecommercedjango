

# coding=utf-8
from django.test import TestCase, Client



class IndexViewTestCase(TestCase):

	def IndexViewTestCase(TestCase):
		def test_status_code(self):
			client = Client()
			response = client.get('/')
			self.assertEquals(response.stataus_code, 200)
