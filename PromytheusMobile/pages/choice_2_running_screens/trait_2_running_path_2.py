from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
import time


class RunningJumpingScreen:

    def __init__(self, driver):

        self.driver = driver
        # Choice 1: Loves own company rather than team sports
        self.choice_1_prefer_own_company = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((MobileBy.XPATH, "//android.view.View[@bounds='[920,322][1006,408]']")))
        # Choice 2: Do they love playing in a team?
        self.choice_2_prefer_team = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((MobileBy.XPATH, "//android.view.View[@bounds='[920,548][1006,634]']")))

    def select_choice_1_prefer_own_company(self):
        self.choice_1_prefer_own_company.click()

    def select_choice_2_prefer_team(self):
        self.choice_2_prefer_team.click()

    def click_next_btn(self):
        ele = self.driver.find_element_by_id("com.promytheus.findmytalent:id/button_next")
        ele.click()
        time.sleep(2)
