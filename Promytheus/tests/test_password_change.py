from selenium import webdriver
import time
import json
import unittest
import HtmlTestRunner
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from browsers.browser import Browser
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.profile_page import MyProfilePage


class TestPasswordChangePage(unittest.TestCase):

    global data
    with open("C:/Users/jolee/Desktop/Selenium/Promytheus/testdata/test_data.json",
              encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
    global appURL
    appURL =  "https://app.promytheus.net/sign-in.html"

    @classmethod
    def setUpClass(cls):
        b = Browser()
        cls.driver = webdriver.Chrome(executable_path=b.chrome)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)

    def test_01_password_change_valid_input(self):
        # Verify user can change password after entering valid input
        driver = self.driver
        driver.get(appURL)
        login = LoginPage(driver)
        login.enter_email(data['login_test_data']['user_1']['email'])
        login.enter_password(data['login_test_data']['user_1']['password'])
        login.click_login_button()
        time.sleep(1)

        home = HomePage(driver)
        home.click_user_icon()
        home.click_my_profile_link()
        time.sleep(1)

        profile = MyProfilePage(driver)
        profile.click_pass_change_tab_link()
        profile.enter_current_password(data['login_test_data']['user_1']['password'])
        profile.enter_new_password(data['login_test_data']['user_1']['password_2'])
        profile.enter_confirm_password(data['login_test_data']['user_1']['password_2'])
        time.sleep(1)
        profile.click_update_button()
        message = profile.confirm_update_pass_message()
        self.assertEqual(message, "Password changed successfully.")
        profile.click_confirm_popup_ok_button()
        time.sleep(1)
        profile.click_p_user_icon()
        profile.click_p_sign_out()

    def test_03_password_change_back(self):
        # Verify user can change password back to original password following same steps
        driver = self.driver
        driver.get(appURL)
        login = LoginPage(driver)
        login.enter_email(data['login_test_data']['user_1']['email'])
        login.enter_password(data['login_test_data']['user_1']['password_2'])
        login.click_login_button()
        time.sleep(1)

        home = HomePage(driver)
        home.click_user_icon()
        home.click_my_profile_link()
        time.sleep(1)

        profile = MyProfilePage(driver)
        profile.click_pass_change_tab_link()
        profile.enter_current_password(data['login_test_data']['user_1']['password_2'])
        profile.enter_new_password(data['login_test_data']['user_1']['password'])
        profile.enter_confirm_password(data['login_test_data']['user_1']['password'])
        time.sleep(1)
        profile.click_update_button()
        message = profile.confirm_update_pass_message()
        self.assertEqual(message, "Password changed successfully.")
        profile.click_confirm_popup_ok_button()
        time.sleep(1)
        profile.click_p_user_icon()
        profile.click_p_sign_out()

    def test_02_unsuccessful_password_change_blank_curr_pass(self):
        # Verify user receives error message if incorrect current password entered
        driver = self.driver
        driver.get(appURL)
        login = LoginPage(driver)
        login.enter_email(data['login_test_data']['user_1']['email'])
        login.enter_password(data['login_test_data']['user_1']['password'])
        login.click_login_button()
        message = login.check_invalid_user_error_message()
        self.assertEqual(message, "Invalid Email or Password.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete")


if __name__ == '__main__':
    unittest.main()


# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
#         output='C:/Users/jolee/PycharmProjects/MySelProject/Promytheus/reports'))


        # Verify user receives error message if new password does not meeting requirements
        # Verify user receives error message if confirm password does not match new password
        # Verify user cannot leave current password field blank
        # Verify user cannot leave new password field blank
        # Verify user cannot leave confirm password field blank
