from selenium import webdriver
import unittest
import time
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from Promytheus.pages.login_page import LoginPage
from Promytheus.pages.home_page import HomePage
from Promytheus.browsers.browser import Browser


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        b = Browser()
        cls.driver = webdriver.Chrome(executable_path=b.chrome)
        cls.driver.delete_all_cookies()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    def test_01_login_valid(self):

        # Test Case 1: Verify successful login with valid email/valid password
        driver = self.driver
        driver.get("https://app.promytheus.net")
        time.sleep(1)
        login = LoginPage(driver)
        login.enter_email("jolee.test1@gmail.com")
        login.enter_password("password")
        login.click_login_button()

        homepage = HomePage(driver)
        # Verify user is in homepage
        time.sleep(1)
        title = driver.title
        self.assertEqual(title, "ProMytheUs - Talents")
        homepage.click_user_icon()
        homepage.click_sign_out()

    def test_02_login_invalid_email(self):
        # Test Case 2: Verify unsuccessful login/expected error message with invalid email/valid password
        driver = self.driver
        driver.get("https://app.promytheus.net")
        time.sleep(1)
        login = LoginPage(driver)
        login.enter_email("jolee.test1@gmail.com1")
        login.enter_password("password")
        login.click_login_button()
        # Verify expected error message
        message = login.check_invalid_email_or_pass_error_message()
        self.assertEqual(message, "Invalid Email or Password.")

    def test_03_login_invalid_password(self):
        # Test Case 3: Verify unsuccessful login/expected error message with valid email/invalid password
        driver = self.driver
        driver.get("https://app.promytheus.net")
        time.sleep(1)
        login = LoginPage(driver)
        login.enter_email("jolee.test1@gmail.com")
        login.enter_password("password1")
        login.click_login_button()
        message = login.check_invalid_email_or_pass_error_message()
        self.assertEqual(message, "Invalid Email or Password.")

    def test_04_login_blank_email(self):
        # Test Case 4: Verify unsuccessful login/expected error message with blank email/valid password
        driver = self.driver
        driver.get("https://app.promytheus.net")
        time.sleep(1)
        login = LoginPage(driver)
        # Enter blank email
        login.enter_password("password")
        login.click_login_button()
        time.sleep(1)
        message = login.check_blank_email_error_message()
        self.assertEqual(message, "This value is required.")

    def test_05_login_blank_pass(self):
        # Test Case 5: Verify unsuccessful login/expected error message with valid email/blank password
        driver = self.driver
        driver.get("https://app.promytheus.net")
        time.sleep(1)
        login = LoginPage(driver)
        login.enter_email("jolee.test1@gmail.com")
        login.click_login_button()
        time.sleep(1)
        message = login.check_blank_pass_error_message()
        self.assertEqual(message, "This value is required.")

    def test_06_login_blank_email_blank_pass(self):
        # Test Case 6: Verify unsuccessful login/expected error messages with blank email/blank password
        driver = self.driver
        driver.get("https://app.promytheus.net")
        time.sleep(1)
        login = LoginPage(driver)
        login.click_login_button()
        time.sleep(1)
        msg_email = login.check_blank_email_error_message()
        self.assertEqual(msg_email, "This value is required.")
        msg_pass = login.check_blank_pass_error_message()
        self.assertEqual(msg_pass, "This value is required.")

    def test_07_nav_register_page_click_register_button(self):
        # Test Case 7: Verify user navigates to Registration page if user click Register Now button
        driver = self.driver
        driver.get("https://app.promytheus.net")
        time.sleep(1)
        login = LoginPage(driver)
        login.click_register_button()
        time.sleep(1)
        title = driver.title
        self.assertEqual(title, "ProMytheUs - Sign Up")
        driver.back()

    def test_08_nav_pass_reset_page_click_forgot_pass_link(self):
        # Test Case 7: Verify user navigates to Password Reset page if user click Forgot your password? link
        driver = self.driver
        driver.get("https://app.promytheus.net")
        time.sleep(1)
        login = LoginPage(driver)
        login.click_reset_password_link()
        time.sleep(1)
        title = driver.title
        self.assertEqual(title, "ProMytheUs - Password Reset")
        driver.back()

    @classmethod
    def tearDownClass(cls):
        # Close window
        cls.driver.close()
        # Quit Driver
        cls.driver.quit()
        print("Test Complete")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=
                                                           "C:/Users/jolee/AppData/Local/Programs/Python/Python37-32/Bootcamp/SampleProjects/Promytheus/reports"))
