from logging import log
from unittest.case import skip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from django.test import LiveServerTestCase


MAX_WAIT = 10

class FunctionalTest(LiveServerTestCase):
    def setUp(self):
        options = Options()
        options.binary_location = r'C:/Program Files/Mozilla Firefox/firefox.exe'
        self.browser = webdriver.Firefox(options=options)

    def tearDown(self):
        self.browser.quit()

    def testStarting(self):
        self.browser.get(self.live_server_url)

        self.assertIn('Welcome', self.browser.title)

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:  
            try:
                table = self.browser.find_element_by_id('theTable')  
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return  
            except (AssertionError, WebDriverException) as e:  
                if time.time() - start_time > MAX_WAIT:  
                    raise e  
                time.sleep(0.5)  

    def testMainPageCorrect(self):
        self.browser.get(self.live_server_url)

        try:
            welcomeText = self.browser.find_element_by_id("welcomeTxt")
            self.assertIn('Welcome', welcomeText.text)
        except:
            self.assertTrue(False, "Element 'Welcome' doesn't exist.")

        try:
            loginBtn = self.browser.find_element_by_id('loginBtn')
        except:
            self.assertTrue(False, "Element 'loginBtn' doesn't exits.")
        try:
            registerBtn = self.browser.find_element_by_id('registerBtn')
        except:
            self.assertTrue(False, "Element 'registerBtn' doesn't exits.")

    def testLoginPage(self):
        self.browser.get(self.live_server_url)

        try:
            loginBtn = self.browser.find_element_by_id('loginBtn')
        except:
            self.assertTrue(False, "Element 'loginBtn' doesn't exits.")

        loginBtn.click()

        self.assertIn('Login', self.browser.title)

    def testLoginHTML(self):
        self.browser.get(self.live_server_url)

        try:
            loginBtn = self.browser.find_element_by_id('loginBtn')
        except:
            self.assertTrue(False, "Element 'loginBtn' doesn't exits.")

        loginBtn.click()

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
        self.browser.get(self.live_server_url)

        try:
            loginBtn = self.browser.find_element_by_id('loginBtn')
        except:
            self.assertTrue(False, "Element 'loginBtn' doesn't exits.")

        loginBtn.click()

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
        self.browser.get(self.live_server_url)

        try:
            loginBtn = self.browser.find_element_by_id('loginBtn')
        except:
            self.assertTrue(False, "Element 'loginBtn' doesn't exits.")

        loginBtn.click()

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

        try:
            recipeSubmit = self.browser.find_element_by_id("submitBtn")
        except:
            self.assertTrue(False, "Element 'submitBtn' doesn't exist on recipe page.")

        try:
            recipeName = self.browser.find_element_by_id("name")
        except:
            self.assertTrue(False, "Element 'name' doesn't exist on recipe page.")

        try:
            recipeDirections = self.browser.find_element_by_id("directions")
        except:
            self.assertTrue(False, "Element 'directions' doesn't exist on recipe page.")

        try:
            recipeIng = self.browser.find_element_by_id("ingredients")
        except:
            self.assertTrue(False, "Element 'directions' doesn't exist on recipe page.")

        try:
            recipeTable = self.browser.find_element_by_id("theTable")
        except:
            self.assertTrue(False, "Element 'theTable' doesn't exist on recipe page.")

        self.assertIn(theName, self.browser.title)

    @skip
    def testTableWritingData(self):
        self.browser.get(self.live_server_url)
        theName = "some name"
        theDirections = "These are some directions to make this amazing recipe for some great food."
        theIngredients = "Some ingredients"

        try:
            loginBtn = self.browser.find_element_by_id('loginBtn')
        except:
            self.assertTrue(False, "Element 'loginBtn' doesn't exits.")

        loginBtn.click()

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

        recipeSubmit = self.browser.find_element_by_id("submitBtn")
        recipeName = self.browser.find_element_by_id("name")
        recipeDirections = self.browser.find_element_by_id("directions")
        recipeIng = self.browser.find_element_by_id("ingredients")

        recipeName.send_keys(theName)
        recipeDirections.send_keys(theDirections)
        recipeIng.send_keys(theIngredients)

        self.wait_for_row_in_list_table(theName)


