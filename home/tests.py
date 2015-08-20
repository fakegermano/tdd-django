from django.http import HttpRequest
from django.test import TestCase

from home.views import home_page
# Create your tests here.
class HomePageViewTest(TestCase):

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertIn('<title>Home Conpec</title>', response.content.decode('utf8'))
        self.assertTrue(response.content.startswith('<html>'.encode('utf8')))
        self.assertTrue(response.content.endswith('</html>'.encode('utf8')))
