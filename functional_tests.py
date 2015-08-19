from selenium import webdriver

#basic test to check if django is installed
browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Django' in browser.title