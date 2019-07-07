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
        driver.get("https://app.promytheus.net")                                                            # Go to website
        time.sleep(1)                                                                                       # I'm getting errors, so I added wait time

        login = LoginPage(driver)                                                                           # Call instance of LoginPage class
        login.enter_email(valid_email)                                                                      # Enter valid email in email field
        login.enter_password(valid_password)                                                                # Enter valid password in password field
        login.click_login_button()                                                                          # Click the login button

        homepage = HomePage(driver)                                                                         # Call instance of HomePage class
        time.sleep(1)                                                                                       # Title page takes some time to change
        title = driver.title                                                                                # Get title of page
        self.assertEqual(title, "ProMytheUs - Talents")                                                     # Verifying title of page matches title of homepage (To verify we successfully logged in)
        homepage.click_user_icon()                                                                          # Click user icon
        homepage.click_sign_out()                                                                           # Click sign out link

    def test_02_login_invalid_email(self):
        # Test Case 2: Verify unsuccessful login/expected error message with invalid email/valid password
        driver = self.driver
        driver.get("https://app.promytheus.net")                                                            # Go to website
        login = LoginPage(driver)                                                                           # Call instance of LoginPage class
        login.enter_email(invalid_email)                                                                    # Enter invalid email in email field
        login.enter_password(valid_password)                                                                # Enter valid password in password field
        login.click_login_button()                                                                          # Click the login button
        message = login.check_invalid_email_or_pass_error_message()                                         # Get error message and assign to variable
        self.assertEqual(message, "Invalid Email or Password.")                                             # Verify with expected error message

    def test_03_login_invalid_password(self):
        # Test Case 3: Verify unsuccessful login/expected error message with valid email/invalid password
        driver = self.driver
        driver.get("https://app.promytheus.net")                                                            # Go to website
        login = LoginPage(driver)                                                                           # Call instance of LoginPage class
        login.enter_email(valid_email)                                                                      # Enter valid email in email field
        login.enter_password(invalid_password)                                                              # Enter invalid password in password field
        login.click_login_button()                                                                          # Click the login button
        message = login.check_invalid_email_or_pass_error_message()                                         # Get error message and assign to variable
        self.assertEqual(message, "Invalid Email or Password.")                                             # Verify with expected error message

    def test_04_login_blank_email(self):
        # Test Case 4: Verify unsuccessful login/expected error message with blank email/valid password
        driver = self.driver
        driver.get("https://app.promytheus.net")
        login = LoginPage(driver)
        # Enter blank email
        login.enter_password(valid_password)
        login.click_login_button()
        time.sleep(1)
        message = login.check_blank_email_error_message()
        self.assertEqual(message, "This value is required.")

    def test_05_login_blank_pass(self):
        # Test Case 5: Verify unsuccessful login/expected error message with valid email/blank password
        driver = self.driver
        driver.get("https://app.promytheus.net")
        login = LoginPage(driver)
        login.enter_email(valid_email)
        login.click_login_button()
        time.sleep(1)
        message = login.check_blank_pass_error_message()
        self.assertEqual(message, "This value is required.")

    def test_06_login_blank_email_blank_pass(self):
        # Test Case 6: Verify unsuccessful login/expected error messages with blank email/blank password
        driver = self.driver
        driver.get("https://app.promytheus.net")
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
        login = LoginPage(driver)
        login.click_register_button()
        title = driver.title
        self.assertEqual(title, "ProMytheUs - Sign Up")
        driver.back()

    def test_08_nav_pass_reset_page_click_forgot_pass_link(self):
        # Test Case 7: Verify user navigates to Password Reset page if user click Forgot your password? link
        driver = self.driver
        driver.get("https://app.promytheus.net")
        login = LoginPage(driver)
        login.click_reset_password_link()
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
                                                           "/Users/jabeentausia/PycharmProjects/Promytheus/MySelProject/Promytheus/reports"))
