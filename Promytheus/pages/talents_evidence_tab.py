from locators.locators import Locators
from pages.talents_category_tab import TalentsForm

import time


class TalentsEvidence:

    def __init__(self, driver):
        self.driver = driver

        # ----------------------------------- Elements -----------------------------------

        # Evidence tab link
        self.evidence_tab_link_xpath = Locators.evidence_tab_link_xpath

        # Testimonies of people who know talent
        self.testimony_checkbox_family_xpath = Locators.testimony_checkbox_family_xpath
        self.testimony_checkbox_friends_xpath = Locators.testimony_checkbox_friends_xpath
        self.testimony_checkbox_teachers_xpath = Locators.testimony_checkbox_teachers_xpath
        self.testimony_checkbox_coworkers_xpath = Locators.testimony_checkbox_coworkers_xpath

        self.testimony_family_textbox_01_xpath = Locators.testimony_family_textbox_01_xpath
        self.family_01_upload_btn_name = Locators.family_01_upload_file_btn_name

        self.talent_work_product_textfield_xpath = Locators.talent_work_product_textfield_xpath
        self.talent_work_product_upload_file_btn_xpath = Locators.talent_work_product_upload_file_btn_xpath

        self.evidence_tab_next_btn = Locators.evidence_tab_next_btn

        # ----------------------------------- Methods -----------------------------------

    def click_evidence_tab_link(self):
        self.driver.find_element_by_xpath(self.evidence_tab_link_xpath).click()

    def click_family_checkbox(self):
        self.driver.find_element_by_xpath(self.testimony_checkbox_family_xpath).click()

    def click_teachers_checkbox(self):
        self.driver.find_element_by_xpath(self.testimony_checkbox_teachers_xpath).click()

    def click_friends_checkbox(self):
        self.driver.find_element_by_xpath(self.testimony_checkbox_friends_xpath).click()

    def click_coworkers_checkbox(self):
        self.driver.find_element_by_xpath(self.testimony_checkbox_coworkers_xpath).click()

    def enter_text_in_testimony_family_text_box_01(self, text):
        self.driver.find_element_by_xpath(self.testimony_family_textbox_01_xpath).click()
        self.driver.find_element_by_xpath(self.testimony_family_textbox_01_xpath).clear()
        self.driver.find_element_by_xpath(self.testimony_family_textbox_01_xpath).send_keys(text)

    def enter_text_in_talent_work_product_field(self, text):
        self.driver.find_element_by_xpath(self.talent_work_product_textfield_xpath).click()
        self.driver.find_element_by_xpath(self.talent_work_product_textfield_xpath).clear()
        self.driver.find_element_by_xpath(self.talent_work_product_textfield_xpath).send_keys(text)

    def upload_file_family_01_field(self, file_path):
        self.driver.find_element_by_name(self.family_01_upload_btn_name).send_keys(file_path)

    def upload_file_talent_work_product_field(self, file_path):
        self.driver.find_element_by_xpath(self.talent_work_product_upload_file_btn_xpath).send_keys(file_path)

    def nav_evidence_tab(self):
        self.click_evidence_tab_link()
        self.click_family_checkbox()
        # if not self.driver.find_element_by_xpath(self.testimony_checkbox_family_xpath).is_selected():
        #     self.click_family_checkbox()
        # else:
        #     self.click_family_checkbox()
        #     self.click_family_checkbox()
        time.sleep(1)
        self.click_teachers_checkbox()
        self.click_friends_checkbox()
        self.click_coworkers_checkbox()
        self.click_coworkers_checkbox()
        self.click_friends_checkbox()
        self.click_teachers_checkbox()
        time.sleep(1)
        self.enter_text_in_testimony_family_text_box_01("Testing")
        time.sleep(1)
        self.upload_file_family_01_field("C:/Users/jolee/Desktop/Moon_Chae-Won-p001.jpg")
        time.sleep(2)
        self.enter_text_in_talent_work_product_field("Testing")
        time.sleep(1)
        self.upload_file_talent_work_product_field("C:/Users/jolee/Desktop/Moon_Chae-Won-p001.jpg")
        time.sleep(1)

        # Clean up
        self.driver.find_element_by_xpath(self.testimony_family_textbox_01_xpath).clear()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.talent_work_product_textfield_xpath).clear()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.testimony_checkbox_family_xpath).click()
        time.sleep(1)

        self.evidence_tab_next_btn.click()
