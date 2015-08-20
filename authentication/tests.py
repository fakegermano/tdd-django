from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from authentication.models import ConpecUser

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
        request.POST['password'] = 'test'

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
        request.POST['password'] = 'test'

        # Send to the view
        response = login_page(request)

        # Send context to the template
        expected_content = render_to_string('login.html', {'login_status': 'Login Failed!'})

        # Test if content is as expected
        self.assertEqual(expected_content, response.content.decode('utf8'))


class UserModelTest(TestCase):

    def setUp(self):
        self.test_user = ConpecUser()
        self.test_user.user = User.objects.create_user(username='teste', email='teste@teste.com')
        self.test_user.user.set_password('teste')
        self.test_user.user.save()
        self.test_user.ra = '123456'
        self.test_user.save()

    def test_saving_and_retrieving_users(self):
        first_user = ConpecUser()
        first_user.user = User.objects.create_user(username='first', email='first@user.com')
        first_user.ra = '123456'
        first_user.save()

        second_user = ConpecUser()
        second_user.user = User.objects.create_user(username='second', email='second@user.com')
        second_user.ra = '654321'
        second_user.save()

        saved_users = ConpecUser.objects.all()
        self.assertEqual(saved_users.count(), 3)

        first_saved_user = saved_users[1]
        second_saved_user = saved_users[2]
        self.assertEqual(str(first_saved_user), 'first-123456')
        self.assertEqual(str(second_saved_user), 'second-654321')

    def test_user_login(self):
        # Test login success
        username = 'test'
        password = 'test'
        user = authenticate(username=username, password=password)
        self.assertTrue(user is not None)
        my_user = ConpecUser.objects.get(user=user)
        self.assertEqual(my_user, self.test_user)

        # Test login Fail by username
        username = 'what'
        user = authenticate(username=username, password=password)
        self.assertTrue(user is None)

        # Test login Fail by password
        username = 'test'
        password = 'what'
        user = authenticate(username=username, password=password)
        self.assertTrue(user is None)




