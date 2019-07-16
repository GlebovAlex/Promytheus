#!/usr/bin/python3
import unittest
import time
import json
# import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".", ".."))
from pages.login_page import LoginPage
from pages.home_page import HomePage
from browsers.browser import Browser


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.headless = True
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.binary_location = '/usr/bin/google-chrome'
        cls.driver = webdriver.Chrome(options=options, executable_path='/usr/bin/chromedriver')
        b = Browser()
        # cls.driver = webdriver.Chrome(executable_path=b.chrome)
        # # cls.driver = webdriver.Firefox(executable_path=b.firefox)
        # cls.driver = webdriver.Edge()
        cls.driver.delete_all_cookies()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    def test_01_success_login_logout_valid_credentials(self):
        # Test Case 1: Verify successful login with valid email/valid password
        with open('Promytheus/testdata/test_data.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
        driver = self.driver
        driver.get("https://app.promytheus.net")
        # time.sleep(1)

        login = LoginPage(driver)
        login.enter_email(data["login_test_data"]["user_1"]["email"])
        login.enter_password(data["login_test_data"]["user_1"]["password"])
        login.click_login_button()
        time.sleep(1)
        home = HomePage(driver)
        title = driver.title
        self.assertEqual(title, "ProMytheUs - Talents")
        home.click_user_icon()
        home.click_sign_out()

    def test_02_unsuccessful_login_invalid_email(self):
        # Test Case 2: Verify unsuccessful login/expected error message with invalid email/valid password
        with open('Promytheus/testdata/test_data.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
        driver = self.driver
        driver.get("https://app.promytheus.net")
        login = LoginPage(driver)
        login.enter_email(data['login_test_data']['invalid_user']['email'])
        login.enter_password(data['login_test_data']['user_1']['password'])
        login.click_login_button()
        message = login.check_invalid_user_error_message()
        self.assertEqual(message, "Invalid Email or Password.")

    def test_03_unsuccessful_login_invalid_password(self):
        # Test Case 3: Verify unsuccessful login/expected error message with valid email/invalid password
        with open('Promytheus/testdata/test_data.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
        driver = self.driver
        driver.get("https://app.promytheus.net")
        login = LoginPage(driver)
        login.enter_email(data['login_test_data']['user_1']['email'])
        login.enter_password(data['login_test_data']['invalid_user']['password'])
        login.click_login_button()
        message = login.check_invalid_user_error_message()
        self.assertEqual(message, "Invalid Email or Password.")

    def test_04_unsuccessful_login_blank_email(self):
        # Test Case 4: Verify unsuccessful login/expected error message with blank email/valid password
        with open('Promytheus/testdata/test_data.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
        driver = self.driver
        driver.get("https://app.promytheus.net")
        login = LoginPage(driver)
        # Enter blank email
        login.enter_password(data['login_test_data']['user_1']['password'])
        login.click_login_button()
        time.sleep(1)
        message = login.check_blank_email_error_message()
        self.assertEqual(message, "This value is required.")

    def test_05_unsuccessful_login_blank_pass(self):
        # Test Case 5: Verify unsuccessful login/expected error message with valid email/blank password
        with open('Promytheus/testdata/test_data.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
        driver = self.driver
        driver.get("https://app.promytheus.net")
        login = LoginPage(driver)
        login.enter_email(data['login_test_data']['user_1']['email'])
        login.click_login_button()
        time.sleep(1)
        message = login.check_blank_pass_error_message()
        self.assertEqual(message, "This value is required.")

    def test_06_unsuccessful_login_blank_email_blank_pass(self):
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

    def test_07_unsuccessful_login_unconfirmed_email(self):
        # Test Case 8: Verify unsuccessful login with valid but unconfirmed email
        with open('Promytheus/testdata/test_data.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
        driver = self.driver
        driver.get("https://app.promytheus.net")
        login = LoginPage(driver)
        login.enter_email(data['login_test_data']['user_3_uce']['email'])
        login.enter_password(data['login_test_data']['user_3_uce']['password'])
        login.click_login_button()
        time.sleep(1)
        msg_unconfirmed = login.check_unconfirmed_email_error_message()
        self.assertEqual(msg_unconfirmed, "The email is not confirmed.")

    def test_08_unsuccessful_login_userA_email_userB_pass(self):
        # Test Case 8: Verify unsuccessful login with valid userA email/valid userB password
        # Assume user 2 password different than user 1 password
        with open('Promytheus/testdata/test_data.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
        driver = self.driver
        driver.get("https://app.promytheus.net")
        login = LoginPage(driver)
        login.enter_email(data['login_test_data']['user_1']['email'])
        login.enter_password(data['login_test_data']['user_2_new']['password'])
        login.click_login_button()
        time.sleep(1)
        message = login.check_invalid_user_error_message()
        self.assertEqual(message, "Invalid Email or Password.")

    def test_09_nav_register_page(self):
        # Test Case 7: Verify user navigates to Registration page if user click Register Now button
        driver = self.driver
        driver.get("https://app.promytheus.net")
        login = LoginPage(driver)
        login.click_register_button()
        title = driver.title
        self.assertEqual(title, "ProMytheUs - Sign Up")
        driver.back()

    def test_10_nav_pass_reset_page(self):
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
    unittest.main()

# if __name__ == '__main__':
#      unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=
#                                                             "C:/Users/jolee/PyCharmProjects/MySelProject/Promytheus/reports"))
#
# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=
#                                                            "/Users/jabeentausia/PycharmProjects/Promytheus/MySelProject/Promytheus/reports"))
