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
        request = HttpRequest()
        request.method = 'POST'
        request.POST['username'] = ''
        request.POST['password'] = ''
        response = login_page(request)
        expected_content = render_to_string('login.html', {'error_messages': 'Username and Password missing!'})
        self.assertEqual(expected_content, response.content.decode('utf8'))

    def test_login_page_can_login_only_username(self):
        # Create a request
        request = HttpRequest()
        request.method = 'POST'
        request.POST['username'] = 'user.name'
        request.POST['password'] = ''
        response = login_page(request)
        expected_content = render_to_string('login.html', {'error_messages': 'Password missing!'})
        self.assertEqual(expected_content, response.content.decode('utf8'))

    def test_login_page_can_login_only_password(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['username'] = ''
        request.POST['password'] = 'teste'
        response = login_page(request)
        expected_content = render_to_string('login.html', {'error_messages': 'Username missing!'})
        self.assertEqual(expected_content, response.content.decode('utf8'))

    def test_login_page_can_login(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['username'] = 'user.name'
        request.POST['password'] = 'teste'
        response = login_page(request)
        expected_content = render_to_string('login.html', {'login_status': 'Login Successfull!'})
        self.assertEqual(expected_content, response.content.decode('utf8'))

