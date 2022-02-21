from django.test import TestCase, Client

from django.urls import reverse, resolve

from .views import *

# Create your tests here.




class TestUrls(TestCase):

    def test_login_url(self):

        url = reverse('login')

        self.assertEquals(resolve(url).func, login)



    def test_register_url(self):

        url = reverse('register')

        self.assertEquals(resolve(url).func, register)



    def test_contact_url(self):

        url = reverse('contact')

        self.assertEquals(resolve(url).func, contact)



    def test_product_url(self):

        url = reverse('product')

        self.assertEquals(resolve(url).func, product)



