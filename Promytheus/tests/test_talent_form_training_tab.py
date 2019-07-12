from selenium import webdriver
from browsers.browser import Browser
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.talents_training_tab import TalentsTraining
import time
import unittest
from selenium.webdriver.support.ui import Select


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
        time.sleep(2)
        login = LoginPage(driver)
        login.login()

        # Click Edit icon on Talents Home Page for item 1
        home = HomePage(driver)
        time.sleep(3)
        home.click_talent_01_edit_icon()
        time.sleep(3)
        # Click Training tab link

        tr = TalentsTraining(driver)
        tr.click_training_tab_link()
        time.sleep(1)

        # Selecting through the dropdown menu for Training History
        ele = driver.find_element_by_xpath(tr.training_history_select_xpath)
        ele.click()
        time.sleep(1)
        ele.click()
        drop = Select(ele)
        drop.select_by_visible_text("None")
        drop.select_by_visible_text("Less than a year")
        drop.select_by_index(2)
        drop.select_by_value("MORE_2_YEARS")
        drop.select_by_index(4)
        drop.select_by_index(5)
        drop.select_by_index(6)

        # Click Yes/No in Professionally Coached
        tr.click_prof_coached_yes()
        tr.click_prof_coached_no()
        tr.click_prof_coached_yes()

        # Under Professionally Coached, enter in text field
        tr.enter_name_coached_field("Testing")
        time.sleep(1)
        tr.enter_success_level_coached_field("Testing")
        time.sleep(1)
        # Click Sometimes/Intensive button Training Type
        tr.click_training_type_intensive()
        tr.click_training_type_sometimes()

        # Enter in the text field of School or College
        tr.enter_school_field("Testing")
        time.sleep(1)
        tr.enter_success_level_field("Testing")

        # Click Skill level radio buttons
        tr.click_beginner_skill_level_radio()
        tr.click_advanced_skill_level_radio()
        tr.click_pro_skill_level_radio()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("-------------------- Test Complete --------------------")


if __name__ == "__main__":
    unittest.main()
