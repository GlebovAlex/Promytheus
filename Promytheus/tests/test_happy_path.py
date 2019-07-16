#!/usr/bin/python3
from selenium import webdriver
import unittest
import time
# import HtmlTestRunner
import json
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".", ".."))
from pages.login_page import LoginPage
from browsers.browser import Browser
from pages.personal_page import TalentPage
from pages.talenttrait_page import TraitsPage
from pages.talents_category_tab import TalentsForm
from pages.talents_evidence_tab import TalentsEvidence
from pages.talents_training_tab import TalentsTraining
from pages.personalitytraits_page import p_traits


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.headless = True
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.binary_location = '/usr/bin/google-chrome'
        cls.driver = webdriver.Chrome(options=options, executable_path='/usr/bin/chromedriver')
        # b = Browser()
        # cls.driver = webdriver.Chrome(executable_path=b.chrome)
        # # cls.driver = webdriver.Firefox(executable_path=b.firefox)
        # cls.driver = webdriver.Edge()
        cls.driver.delete_all_cookies()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    def test_create_talent_valid(self):
        # with open('/Users/jabeentausia/PycharmProjects/Promytheus/Promytheus/testdata/test_data.json',
        #           encoding='utf-8') as data_file:
        #     data = json.loads(data_file.read())
        with open('Promytheus/testdata/test_data.json',
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
        time.sleep(4)

        # Lavanya
        #personality traits tab
        ptraits = p_traits(driver)
        time.sleep(2)
        ptraits.click_traits_tab()
        time.sleep(2)

        # clicking on the check boxes in the personality traits page
        ptraits.click_chkbx_pttab()
        time.sleep(1)

        # click next button to navigate to story page
        ptraits.click_next_btn()
        time.sleep(2)

        #story tab
        ptraits.enter_age_storytab()
        time.sleep(2)

        #click next button on stroy tab
        ptraits.click_next_button_storytab()
        time.sleep(2)


        # joan
        # Talent Evidence form
        ev = TalentsEvidence(driver)
        ev.click_evidence_tab_link()
        time.sleep(2)
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
        ev.upload_file_family_01_field("Promytheus/tests/Moon_Chae-Won-p001.jpg")
        time.sleep(2)
        ev.enter_text_in_talent_work_product_field("Testing")
        time.sleep(1)
        ev.upload_file_talent_work_product_field("Promytheus/tests/Moon_Chae-Won-p001.jpg")
        time.sleep(1)

        t = TalentsForm(driver)
        time.sleep(1)
        t.click_next_btn()
        time.sleep(2)

        # Talent Training Form
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
        ptraits.click_next_btn()
        time.sleep(3)
        ptraits.click_next_btn()
        time.sleep(3)

        driver.find_element_by_xpath("//div[@class='form-wizard-footer']//button[@class='btn btn-primary ng-binding'][contains(text(),'Finish')] ").click()
        time.sleep(2)
        driver.find_element_by_xpath("//button[@class='cancel']").click()

    @classmethod
    def tearDownClass(cls):
        # Close window
        # cls.driver.close()
        # Quit Driver
        # cls.driver.quit()
        print("Test Complete")


if __name__ == '__main__':
    unittest.main()
