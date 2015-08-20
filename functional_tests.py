
import unittest
from django.core.urlresolvers import reverse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class HomePageTest(unittest.TestCase):

    # Creates the webbrowser on init of every test method
    def setUp(self):
        self.browser = webdriver.Firefox()

    # Close the browser at the end of every test method
    def tearDown(self):
        self.browser.close()

    def test_login_page(self):
        # Basic test to see if the login page works
        self.browser.get('http://localhost:8000/login/')

        # Test to assert the title of the login page
        self.assertIn('Login', self.browser.title)

        # Test to check if there is a header with right content
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('Login', header.text)

        # Test to check if there is a username_input_box in the page
        username_input_box = self.browser.find_element_by_id('id_username')
        self.assertEqual(
            username_input_box.get_attribute('placeholder'),
            'Username'
        )
        # Test to check if there is a password_input_box in the page
        password_input_box = self.browser.find_element_by_id('id_password')
        self.assertEqual(
            password_input_box.get_attribute('placeholder'),
            'Password'
        )

        submit_input_box = self.browser.find_element_by_id('id_submit')
        self.assertEqual(
            submit_input_box.get_attribute('value'),
            'Login'
        )

        username_input_box.send_keys('user.name')
        username_input_box.send_keys(Keys.ENTER)

        error_messages = self.browser.find_element_by_id('id_error_messages')
        self.assertIn(
            'Password missing!',
            error_messages.text
        )

        password_input_box = self.browser.find_element_by_id('id_password')
        password_input_box.send_keys('teste')
        password_input_box.send_keys(Keys.ENTER)

        error_messages = self.browser.find_element_by_id('id_error_messages')
        self.assertIn(
            'Username missing!',
            error_messages.text
        )

        submit_input_box = self.browser.find_element_by_id('id_submit')
        submit_input_box.click()

        error_messages = self.browser.find_element_by_id('id_error_messages')
        self.assertIn(
            'Username and Password missing!',
            error_messages.text
        )

        username_input_box = self.browser.find_element_by_id('id_username')
        password_input_box = self.browser.find_element_by_id('id_password')
        submit_input_box = self.browser.find_element_by_id('id_submit')
        username_input_box.send_keys('user.name')
        password_input_box.send_keys('teste')
        submit_input_box.click()

        login_status = self.browser.find_element_by_id('id_login_status')
        self.assertIn(
            'Login Successfull!',
            login_status.text
        )

    def test_home_page(self):
        # Go to the home Page
        self.browser.get('http://localhost:8000')

        # Test to assert that the title ir right
        self.assertIn('Home', self.browser.title)

        # Test to check if there is a header with the right content
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('Home', header.text)

        # Test to check if there is a link for the login page
        login_link = self.browser.find_element_by_tag_name('a')
        self.assertEqual(
            login_link.get_attribute('href'),
            'http://localhost:8000/login/')
        # Try to click the link
        login_link.click()

if __name__ == '__main__':
    unittest.main()
