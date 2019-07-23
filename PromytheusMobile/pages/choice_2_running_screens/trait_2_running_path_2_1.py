from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
import time


class RunningJumpingScreen2:

    def __init__(self, driver):

        self.driver = driver
        # Choice 1: Swims smooth like a knife going through butter?
        self.choice_1_swims = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((MobileBy.XPATH, "//android.view.View[@bounds='[920,322][1006,408]']")))
        # Choice 2: Do they like to practice a particular sport for hours?
        self.choice_2_practice_sport = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((MobileBy.XPATH, "//android.view.View[@bounds='[920,548][1006,634]']")))
        # Choice 3: Has good eyesight
        self.choice_3_good_eyesight = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((MobileBy.XPATH, "//android.view.View[@bounds='[920,774][1006,860]']")))

    def select_choice_1_swims(self):
        self.choice_1_swims.click()

    def select_choice_2_practice_sports(self):
        self.choice_2_practice_sport.click()

    def select_choice_3_has_good_eyesight(self):
        self.choice_3_good_eyesight.click()

    def click_next_btn(self):
        ele = self.driver.find_element_by_id("com.promytheus.findmytalent:id/button_next")
        ele.click()
        time.sleep(2)
