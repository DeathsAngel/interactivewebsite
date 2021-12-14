import unittest
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import HomePage
from django.views.generic.base import View

# Create your tests here.
class HomePageTests(TestCase):
    def testHomePageReview(self):
        found = resolve('/')
        self.assertEqual(found.func, HomePage, 'Home page test failed: ')

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = HomePage(request)  
        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))  

        self.assertTrue(html.strip().endswith('</html>'))