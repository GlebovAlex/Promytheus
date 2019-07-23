from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
import time


class RunningJumpingScreen3:

    def __init__(self, driver):

        self.driver = driver
        # Choice 1: Loves Some Other Athletics
        self.choice_1_other_athletics = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((MobileBy.XPATH, "//android.view.View[@bounds='[920,322][1006,408]']")))
        # Choice 2: Can Contort body into difficult shapes
        self.choice_2_contort_body = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((MobileBy.XPATH, "//android.view.View[@bounds='[920,548][1006,634]']")))
        # Choice 3: Loves Jumping
        self.choice_3_loves_jumping = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((MobileBy.XPATH, "//android.view.View[@bounds='[920,774][1006,860]']")))
        # Choice 4: Loves Running
        self.choice_3_loves_running = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((MobileBy.XPATH, "//android.view.View[@bounds='[920,1000][1006,1086]']")))

    def select_choice_1_other_athletics(self):
        self.choice_1_other_athletics.click()

    def select_choice_2_contort_body(self):
        self.choice_2_contort_body.click()

    def select_choice_3_loves_jumping(self):
        self.choice_3_loves_jumping.click()

    def select_choice_3_loves_running(self):
        self.choice_3_loves_running.click()

    def click_next_btn(self):
        ele = self.driver.find_element_by_id("com.promytheus.findmytalent:id/button_next")
        ele.click()
        time.sleep(2)
