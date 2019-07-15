from selenium import webdriver
import unittest
import time
import HtmlTestRunner
import sys
import os
import json

sys.path.append(os.path.join(os.path.dirname(__file__), ".", "."))
from pages.login_page import LoginPage
from browsers.browser import Browser
from pages.personal_page import TalentPage
from pages.talenttrait_page import TraitsPage
from Promytheus.pages.personalit_traits_page import p_traits


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
        with open('/Users/jabeentausia/PycharmProjects/Promytheus/Promytheus/testdata/test_data.json',
                  encoding='utf-8') as data_file:
            data = json.loads(data_file.read())

        # time.sleep(1)

        # Successful Login
        driver = self.driver
        driver.get("https://app.promytheus.net")  # Go to website
        time.sleep(1)  # I'm getting errors, so I added wait time

        login = LoginPage(driver)
        login.enter_email(data["talent_test_data"]["email"])
        login.enter_password(data["talent_test_data"]["password"])

        login.click_login_button()  # Click the login button

        # Filling the personal tab form
        talent = TalentPage(driver)
        talent.create_talent_personal_tab()
        time.sleep(1)

        # talent trait form
        trait = TraitsPage(driver)
        trait.complete_talent_trait_tab()
        time.sleep(2)

        #personality traits tab
        ptraits = p_traits(driver)
        time.sleep(2)
        ptraits.click_traits_tab()
        time.sleep(2)

        # clicking on the check boxes in the personality traits page
        # ptraits.click_chkbx_pttab()
        # time.sleep(1)

        # click next button to navigate to story page
        ptraits.click_next_btn()
        time.sleep(2)

        #story tab
        ptraits.enter_age_storytab()
        time.sleep(2)

        #click next button on stroy tab
        ptraits.click_next_button_storytab()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        # Close window
        # cls.driver.close()
        # Quit Driver
        # cls.driver.quit()
        print("Test Complete")


if __name__ == '__main__':
    unittest.main()
