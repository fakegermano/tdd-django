import unittest
from selenium import webdriver


class HomePageTest(unittest.TestCase):

    #creates the webbrowser on init of every test method
    def setUp(self):
        self.browser = webdriver.Firefox()

    #close the browser at the end of every test method
    def tearDown(self):
        self.browser.close()

    def test_login_page(self):
        self.browser.get('http://localhost:8000/login/')
        self.assertIn('Login', self.browser.title)
        self.fail('finish de login test')

    def test_home_page(self):
        #basic test to check if the home page works
        self.browser.get('http://localhost:8000')
        self.assertIn('Conpec', self.browser.title)
        self.fail('finish the home test')

if __name__ == '__main__':
    unittest.main()
