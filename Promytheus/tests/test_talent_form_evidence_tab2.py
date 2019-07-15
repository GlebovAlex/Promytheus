from selenium import webdriver
from browsers.browser import Browser
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.talents_category_tab import TalentsForm
import time
import unittest
from pages.talents_evidence_tab import TalentsEvidence


class TestTalentsEvidenceTab(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        b = Browser()
        cls.driver = webdriver.Chrome(executable_path=b.chrome)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(20)

    def test_01_verify_all_elements_work(self):
        driver = self.driver
        driver.get("https://app.promytheus.net")
        login = LoginPage(driver)
        login.login()
        home = HomePage(driver)
        time.sleep(1)

        # Click Edit icon on Talents Home Page for item 1
        home.click_talent_01_edit_icon()
        time.sleep(2)

        # Click Evidence tab link
        e = TalentsEvidence(driver)
        e.nav_evidence_tab()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("-------------------- Test Complete --------------------")


if __name__ == "__main__":
    unittest.main()
