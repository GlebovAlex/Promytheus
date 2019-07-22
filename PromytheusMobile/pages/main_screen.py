from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
import time


class MainScreen:

    def __init__(self, driver):

        self.driver = driver

        self.choice_1_btn = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((
                MobileBy.XPATH, "//android.view.View[@bounds='[920,322][1006,408]']")))

        self.choice_2_btn = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((
                MobileBy.XPATH, "//android.view.View[@bounds='[920,548][1006,634]']")))

        self.choice_3_btn = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((
                MobileBy.XPATH, "//android.view.View[@bounds='[920,774][1006,860]']")))

        self.choice_4_btn = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((
                MobileBy.XPATH, "//android.view.View[@bounds='[920,1000][1006,1086]']")))

        self.choice_5_btn = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((
                MobileBy.XPATH, "//android.view.View[@bounds='[920,1226][1006,1312]']")))

        self.choice_6_btn = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((
                MobileBy.XPATH, "//android.view.View[@bounds='[920,1452][1006,1538]']")))

        self.choice_7_btn = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((
                MobileBy.XPATH, "//android.view.View[@bounds='[920,1678][1006,1764]']")))

        self.elements = driver.find_elements_by_id("com.promytheus.findmytalent:id/checkbox")

    def click_choice_button(self, choice):
        num = str(choice)
        if num == '1':
            self.choice_1_btn.click()
        elif num == '2':
            self.choice_2_btn.click()
        elif num == '3':
            self.choice_3_btn.click()
        elif num == '4':
            self.choice_4_btn.click()
        elif num == '5':
            self.choice_5_btn.click()
        elif num == '6':
            self.choice_6_btn.click()
        elif num == '7':
            self.choice_7_btn.click()
        else:
            print("Error: Could not understand input. Choice should be between '1-9'.")
        time.sleep(3)

    def click_through_all_buttons(self):
        for element in self.elements:
            element.click()
        time.sleep(3)
