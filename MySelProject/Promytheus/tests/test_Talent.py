from selenium import webdriver
import unittest
import time
import HtmlTestRunner
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Promytheus.pages.login_page import LoginPage
from Promytheus.browsers.browser import Browser
from Promytheus.credentials.cred import valid_email
from Promytheus.credentials.cred import valid_password
from Promytheus.pages.talent_page import TalentPage




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

    def test_create_talent_valid(self):
        #Successful Login
        driver = self.driver
        driver.get("https://app.promytheus.net")  # Go to website
        time.sleep(1)  # I'm getting errors, so I added wait time

        login = LoginPage(driver)  # Call instance of LoginPage class
        login.enter_email(valid_email)  # Enter valid email in email field
        login.enter_password(valid_password)  # Enter valid password in password field
        login.click_login_button()  # Click the login button

        #Creating talent
        talent=TalentPage(driver)
        talent.create_talent()
        time.sleep(1)

        time.sleep(3)  # Title page takes some time to change




    @classmethod
    def tearDownClass(cls):
        # Close window
        #cls.driver.close()
        # Quit Driver
        #cls.driver.quit()
        print("Test Complete")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=
                                                           "C:/Users/jolee/PyCharmProjects/MySelProject/Promytheus//reports"))
