from logging import log
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException

from lists.views import LoginPage 

class FunctionalTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.binary_location = r'C:/Program Files/Mozilla Firefox/firefox.exe'
        self.browser = webdriver.Firefox(options=options)

    def tearDown(self):
        self.browser.quit()

    def testStarting(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('Welcome', self.browser.title)

    def testMainPageCorrect(self):
        self.browser.get('http://localhost:8000')

        try:
            welcomeText = self.browser.find_element_by_id("welcomeTxt")
            self.assertIn('Welcome', welcomeText.text)
        except:
            self.assertTrue(False, "Element 'Welcome' doesn't exist.")
        try:
            welcomeText = self.browser.find_element_by_id("welcomeTxt")
            self.assertIn('Welcome', welcomeText.text)
        except:
            self.assertTrue(False, "Element 'Welcome' doesn't exist.")

    def testLoginPage(self):
        self.browser.get('http://localhost:8000/login')

        self.assertIn('Login', self.browser.title)

    def testLoginHTML(self):
        self.browser.get('http://localhost:8000/login')

        try:
            loginText = self.browser.find_elements_by_id("loginTxt")
            self.assertIn('login', loginText[0].text)
        except:
            self.assertTrue(False, "Element 'loginTxt' doesn't exist.")

        try:
            userNameBox = self.browser.find_elements_by_id("user")
        except:
            self.assertTrue(False, "Element 'user' doesn't exist.")
        else:
            self.assertTrue(True)

        try:
            passBox = self.browser.find_elements_by_id("pass")
        except:
            self.assertTrue(False, "Element 'pass' doesn't exist.")
        else:
            self.assertTrue(True)

        try:
            submitBtn = self.browser.find_elements_by_id("submitBtn")
        except:
            self.assertTrue(False, "Element 'submitBtn' doesn't exist.")
        else:
            self.assertTrue(True)

    def testLoginHTML(self):
        self.browser.get('http://localhost:8000/login')

        userName = self.browser.find_element_by_id("user")
        password = self.browser.find_element_by_id("pass")
        submit = self.browser.find_element_by_id("submitBtn")

        theName = "ItsMe"
        thePass = "ThisIsPassword"

        userName.send_keys(theName)
        password.send_keys(thePass)
        submit.click()

        self.assertIn("Accepted", self.browser.title)

        theText = self.browser.find_element_by_id("confirmText")

        self.assertIn(theName, theText.text)

    def testMyRecipes(self):
        self.browser.get('https://localhost:8000/login')

        userName = self.browser.find_element_by_id("user")
        password = self.browser.find_element_by_id("pass")
        submit = self.browser.find_element_by_id("submitBtn")

        theName = "ItsMe"
        thePass = "ThisIsPassword"

        userName.send_keys(theName)
        password.send_keys(thePass)
        submit.click()

        theLink = self.browser.find_element_by_id("recipeLink")
        theLink.click()

        self.assertIn(theName, self.browser.title)
        self.assertIn(theName, self.browser.title)

if __name__ == '__main__':
    unittest.main()
