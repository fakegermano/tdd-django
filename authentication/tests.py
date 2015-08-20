from django.http import HttpRequest
from django.test import TestCase

from authentication.views import login_page
# Create your tests here.


class LoginPageViewTest(TestCase):

    def test_login_page_returns_correct_html(self):
        request = HttpRequest()
        response = login_page(request)
        self.assertIn('<title>Login Conpec</title>', response.content.decode('utf8'))
        self.assertTrue(response.content.startswith('<html>'.encode('utf8')))
        self.assertTrue(response.content.endswith('</html>'.encode('utf8')))
