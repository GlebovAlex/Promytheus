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
        ev = TalentsEvidence(driver)
        ev.click_evidence_tab_link()
        if not driver.find_element_by_xpath(ev.testimony_checkbox_family_xpath).is_selected():
            ev.click_family_checkbox()
        else:
            ev.click_family_checkbox()
            ev.click_family_checkbox()
        time.sleep(1)
        ev.click_teachers_checkbox()
        ev.click_friends_checkbox()
        ev.click_coworkers_checkbox()
        ev.click_coworkers_checkbox()
        ev.click_friends_checkbox()
        ev.click_teachers_checkbox()
        time.sleep(1)
        ev.enter_text_in_testimony_family_text_box_01("Testing")
        time.sleep(1)
        ev.upload_file_family_01_field("C:/Users/jolee/Desktop/Moon_Chae-Won-p001.jpg")
        time.sleep(2)
        ev.enter_text_in_talent_work_product_field("Testing")
        time.sleep(1)
        ev.upload_file_talent_work_product_field("C:/Users/jolee/Desktop/Moon_Chae-Won-p001.jpg")
        time.sleep(1)

        # Clean up
        driver.find_element_by_xpath(ev.testimony_family_textbox_01_xpath).clear()
        time.sleep(1)
        driver.find_element_by_xpath(ev.talent_work_product_textfield_xpath).clear()
        time.sleep(1)
        driver.find_element_by_xpath(ev.testimony_checkbox_family_xpath).click()
        time.sleep(1)

        t = TalentsForm(driver)
        time.sleep(1)
        t.click_next_btn()
        time.sleep(2)
        t.click_previous_btn()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("-------------------- Test Complete --------------------")


if __name__ == "__main__":
    unittest.main()
