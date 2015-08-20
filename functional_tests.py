
import unittest
from django.core.urlresolvers import reverse
from selenium import webdriver


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

        # Test to check if there is a input_box in the page
        input_box = self.browser.find_element_by_id('id_username')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Username'
        )

        # Try to send only username
        input_box.send_keys('user.name')
        input_box.send_keys('\n')

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
