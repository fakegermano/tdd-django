from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

from authentication.views import login_page
# Create your tests here.


class LoginPageViewTest(TestCase):

    # Test if the login_page returns the correct response
    def test_login_page_uses_template(self):
        # Creates a request
        request = HttpRequest()
        # Send it to the login_page view
        response = login_page(request)

        # Check the content of the file
        expected_content = render_to_string('login.html')
        self.assertEqual(expected_content, response.content.decode('utf8'))

    def test_login_page_can_login_blank(self):
        # Create the request
        request = HttpRequest()

        # Set the method and it's fields
        request.method = 'POST'
        request.POST['username'] = ''
        request.POST['password'] = ''

        # Send to view
        response = login_page(request)

        # Send context dict to template
        expected_content = render_to_string('login.html', {'error_messages': 'Username and Password missing!'})

        # Test if the content is as expected
        self.assertEqual(expected_content, response.content.decode('utf8'))

    def test_login_page_can_login_only_username(self):
        # Create a request
        request = HttpRequest()

        # Set method and the username field
        request.method = 'POST'
        request.POST['username'] = 'user.name'
        request.POST['password'] = ''

        # Send to view
        response = login_page(request)

        # Send context dict to template
        expected_content = render_to_string('login.html', {'error_messages': 'Password missing!'})

        # Test if content is as expected
        self.assertEqual(expected_content, response.content.decode('utf8'))

    def test_login_page_can_login_only_password(self):
        # Create Request
        request = HttpRequest()

        # Set the method and the password field
        request.method = 'POST'
        request.POST['username'] = ''
        request.POST['password'] = 'teste'

        # Send to the view
        response = login_page(request)

        # Send context dict to template
        expected_content = render_to_string('login.html', {'error_messages': 'Username missing!'})

        # Test if content is as expected
        self.assertEqual(expected_content, response.content.decode('utf8'))

    def test_login_page_can_login(self):
        # Create request
        request = HttpRequest()

        # Set the method and values for all fields
        request.method = 'POST'
        request.POST['username'] = 'user.name'
        request.POST['password'] = 'teste'

        # Send to the view
        response = login_page(request)

        # Send context to the template
        expected_content = render_to_string('login.html', {'login_status': 'Login Successfull!'})

        # Test if content is as expected
        self.assertEqual(expected_content, response.content.decode('utf8'))

