from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from authentication.views import login_page
# Create your tests here.


class LoginPageViewTest(TestCase):

    # Test if the login_page returns the correct response
    def test_login_page_returns_correct_html(self):
        # Creates a request
        request = HttpRequest()
        # Send it to the login_page view
        response = login_page(request)

        # Check the content of the file
        expected_content = render_to_string('login.html')
        self.assertEqual(expected_content, response.content.decode('utf8'))
