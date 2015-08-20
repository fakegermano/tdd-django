from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from home.views import home_page
# Create your tests here.


class HomePageViewTest(TestCase):

    # Tests the return of the home page view
    def test_home_page_returns_correct_html(self):
        # Defines a request
        request = HttpRequest()
        # Sends it to home_page view
        response = home_page(request)

        # Check the content of the file
        expected_content = render_to_string('home.html')
        self.assertEqual(expected_content, response.content.decode('utf8'))

