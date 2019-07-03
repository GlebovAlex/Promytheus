from selenium import webdriver
import unittest
import time
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Promytheus.pages.login_page import LoginPage
from Promytheus.pages.home_page import HomePage
from Promytheus.browsers.browser import Browser
from Promytheus.credentials.cred import valid_email
from Promytheus.credentials.cred import valid_password
from Promytheus.credentials.cred import invalid_email
from Promytheus.credentials.cred import invalid_password




class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        b = Browser()
        cls.driver = webdriver.Chrome(executable_path=b.chrome)
        # cls.driver = webdriver.Firefox(executable_path=b.firefox)
        # cls.driver = webdriver.Edge()
        cls.driver.delete_all_cookies()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        # Test Case 1: Verify successful login with valid email/valid password
        driver = self.driver
        driver.get("https://app.promytheus.net")
        time.sleep(1)

        login = LoginPage(driver)
        login.enter_email(valid_email)
        login.enter_password(valid_password)
        login.click_login_button()

        homepage = HomePage(driver)
        time.sleep(1)
        title = driver.title
        self.assertEqual(title, "ProMytheUs - Talents")
        homepage.click_user_icon()
        homepage.click_sign_out()

    def test_02_login_invalid_email(self):
        # Test Case 2: Verify unsuccessful login/expected error message with invalid email/valid password
        driver = self.driver
        driver.get("https://app.promytheus.net")
        login = LoginPage(driver)
        login.enter_email(invalid_email)
        login.enter_password(valid_password)
        login.click_login_button()
        message = login.check_invalid_email_or_pass_error_message()
        self.assertEqual(message, "Invalid Email or Password.")

    def test_03_login_invalid_password(self):
        # Test Case 3: Verify unsuccessful login/expected error message with valid email/invalid password
        driver = self.driver
        driver.get("https://app.promytheus.net")
        login = LoginPage(driver)
        login.enter_email(valid_email)
        login.enter_password(invalid_password)
        login.click_login_button()
        message = login.check_invalid_email_or_pass_error_message()
        self.assertEqual(message, "Invalid Email or Password.")

    @classmethod
    def tearDownClass(cls):
        # Close window
        cls.driver.close()
        # Quit Driver
        cls.driver.quit()
        print("Test Complete")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=
                                                           "C:/Users/jolee/PyCharmProjects/MySelProject/Promytheus/reports"))
