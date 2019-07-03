from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import unittest
import time
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from Promytheus.pages.login_page import LoginPage
from Promytheus.pages.home_page import HomePage
from Promytheus.browsers.browser import Browser


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        b = Browser()
        cls.driver = webdriver.Chrome(executable_path=b.chrome)
        cls.driver.delete_all_cookies()
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver

        # Navigate to web page
        driver.get("https://app.promytheus.net")
        wait = WebDriverWait(driver, 30)

        wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='email']"))).send_keys("jolee.test1@gmail.com")
        # Enter valid password in password text field
        wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='password']"))).send_keys("password")

        wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@id='login']"))).click()

        wait.until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='nav navbar-nav navbar-right']/li[2]/a"))).click()

        wait.until(ec.visibility_of_element_located((By.XPATH, "//ul[@class='nav navbar-nav navbar-right']/li[2]/ul/li/div/a[2]/div/div[2]"))).click()

    @classmethod
    def tearDownClass(cls):
        # Close window
        cls.driver.close()
        # Quit Driver
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=
                                                           "C:/Users/jolee/AppData/Local/Programs/Python/Python37-32/Bootcamp/SampleProjects/Promytheus/reports"))

"""
    def test_02_login_invalid_email(self):
        driver = self.driver

        # Navigate to web page
        driver.get("https://app.promytheus.net")

        login = LoginPage(driver)
        # Enter invalid email in email text field
        login.enter_email("jolee.test1@gmail.com1")
        # Enter valid password in password text field
        login.enter_password("password")
        #time.sleep(1)
        # Click Login button
        login.click_login_button()
        #time.sleep(1)
        # Verify expected error message
        message = login.check_invalid_email_or_pass_error_message()
        self.assertEqual(message, "Invalid Email or Password.")

    def test_03_login_invalid_password(self):
        driver = self.driver

        # Navigate to web page
        driver.get("https://app.promytheus.net")

        login = LoginPage(driver)
        # Enter valid email in email text field
        login.enter_email("jolee.test1@gmail.com")
        # Enter invalid password in password text field
        login.enter_password("password1")
        #time.sleep(1)
        # Click Login button
        login.click_login_button()
        #time.sleep(1)
        # Verify expected error message
        message = login.check_invalid_email_or_pass_error_message()
        time.sleep(1)
        self.assertEqual(message, "Invalid Email or Password.")

    def test_04_login_blank_email(self):
        driver = self.driver

        # Navigate to web page
        driver.get("https://app.promytheus.net")

        login = LoginPage(driver)
        # Enter blank email
        # login.enter_email("jolee.test1@gmail.com")
        # Enter valid password in password text field
        login.enter_password("password")
        #time.sleep(1)
        # Click Login button
        login.click_login_button()
        #time.sleep(1)
        # Verify expected error message
        message = login.check_blank_email_error_message()
        time.sleep(1)
        self.assertEqual(message, "This value is required.")

    def test_04_login_blank_pass(self):
        driver = self.driver

        # Navigate to web page
        driver.get("https://app.promytheus.net")

        login = LoginPage(driver)
        # Enter valid email in email text field
        login.enter_email("jolee.test1@gmail.com")
        # Enter blank password
        #login.enter_password("password")
        #time.sleep(1)
        # Click Login button
        login.click_login_button()
        #time.sleep(1)
        # Verify expected error message
        message = login.check_blank_pass_error_message()
        time.sleep(1)
        self.assertEqual(message, "This value is required.")

"""
