from locators.locators import Locators
import time
from selenium.webdriver.support import ui
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class TalentPage:

    def __init__(self, driver):
        self.driver = driver


        self.new_button=Locators.new_button_xpath
        self.category=Locators.category_xpath
        self.painting=Locators.painting_xpath
        self.next_button=Locators.Next_button_xpath

        self.first_name_xpath = Locators.first_name_xpath
        self.last_name_xpath = Locators.last_name_xpath
        self.Sex_female_xpath = Locators.Sex_female_xpath


        #self.country_name_selection_xpath = Locators.country_name_selection_xpath
        # self.country_option_USA=Locators.country_option_USA
        self.address_line1_xpath=Locators.address_line1_xpath
        self.address_line2_xpath=Locators.address_line2_xpath
        self.city_xpath = Locators.city_xpath
        self.state_xpath = Locators.state_xpath
        self.postalcode_xpath = Locators.postalcode_xpath
        self.contact_email_xpath = Locators.contact_email_xpath
        self.conatct_phone_xpath = Locators.conatct_phone_xpath
        self.height_xpath = Locators.height_xpath
        self.weight_xpath = Locators.weight_xpath
        self.personalPage_next_button_xpath = Locators.personalPage_next_button_xpath

    def create_talent_personal_tab(self):
        self.driver.find_element_by_xpath(self.new_button).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.category).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.painting).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.next_button).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(Locators.first_name_xpath).send_keys("tester1")
        self.driver.find_element_by_xpath(Locators.last_name_xpath).send_keys("testlastname")
        self.driver.find_element_by_xpath(Locators.Sex_female_xpath).click()
        time.sleep(2)

        # countrySelection = ui.WebDriverWait(self.driver, 50).until(
        #     EC.element_to_be_clickable(
        #         (By.XPATH, self.country_name_selection_xpath)))
        #
        # countrySelection.click()

        #self.driver.find_element_by_xpath(self.country_name_selection_xpath).click()
        time.sleep(2)
        # self.driver.find_element_by_xpath(self.country_option_USA).click()
        self.driver.find_element_by_xpath(self.address_line1_xpath).send_keys("123 test rd")
        self.driver.find_element_by_xpath(self.address_line2_xpath).send_keys("apt 1")
        self.driver.find_element_by_xpath(self.city_xpath).send_keys("Walnut Creek")
        self.driver.find_element_by_xpath(self.state_xpath).send_keys("California")
        self.driver.find_element_by_xpath(self.postalcode_xpath).send_keys("94597")
        self.driver.find_element_by_xpath(self.contact_email_xpath).send_keys("test@gmail.com")
        self.driver.find_element_by_xpath(self.conatct_phone_xpath).send_keys("1600400800")
        self.driver.find_element_by_xpath(self.height_xpath).send_keys("5")
        self.driver.find_element_by_xpath(self.weight_xpath).send_keys("120")
        self.driver.find_element_by_xpath(self.personalPage_next_button_xpath).click()

    def create_talent_talenttraits_tab(self):
        self.driver.find_element_by_xpath(self.new_button).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.category).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.painting).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.next_button).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(Locators.first_name_xpath).send_keys("tester1")
        self.driver.find_element_by_xpath(Locators.last_name_xpath).send_keys("testlastname")
        self.driver.find_element_by_xpath(Locators.Sex_female_xpath).click()
        time.sleep(2)

        # countrySelection = ui.WebDriverWait(self.driver, 50).until(
        #     EC.element_to_be_clickable(
        #         (By.XPATH, self.country_name_selection_xpath)))
        #
        # countrySelection.click()

        # self.driver.find_element_by_xpath(self.country_name_selection_xpath).click()
        time.sleep(5)
        # self.driver.find_element_by_xpath(self.country_option_USA).click()
        self.driver.find_element_by_xpath(self.address_line1_xpath).send_keys("123 test rd")
        self.driver.find_element_by_xpath(self.address_line2_xpath).send_keys("apt 1")
        self.driver.find_element_by_xpath(self.city_xpath).send_keys("Walnut Creek")
        self.driver.find_element_by_xpath(self.state_xpath).send_keys("California")
        self.driver.find_element_by_xpath(self.postalcode_xpath).send_keys("94597")
        self.driver.find_element_by_xpath(self.contact_email_xpath).send_keys("test@gmail.com")
        self.driver.find_element_by_xpath(self.conatct_phone_xpath).send_keys("1600400800")
        self.driver.find_element_by_xpath(self.height_xpath).send_keys("5")
        self.driver.find_element_by_xpath(self.weight_xpath).send_keys("120")
        self.driver.find_element_by_xpath(self.personalPage_next_button_xpath).click()