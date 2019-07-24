from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
import time


class MainScreen:

    def __init__(self, driver):

        self.driver = driver

        # Choice 1: Do they wear their emotions on a sleeve? (Are they extremely emotional?)
        self.choice_1_btn_emotional = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((
                MobileBy.XPATH, "//android.view.View[@bounds='[920,322][1006,408]']")))
        # Choice 2: Loves Running/ Jumping
        self.choice_2_btn_running_jumping = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((
                MobileBy.XPATH, "//android.view.View[@bounds='[920,548][1006,634]']")))
        # Choice 3: Connects the dots in things in unique ways - reads between the lines
        self.choice_3_btn_connect_the_dots_in_things_in_unique_ways = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((
                MobileBy.XPATH, "//android.view.View[@bounds='[920,774][1006,860]']")))
        # Choice 4: Do people always love what they cook?
        self.choice_4_btn_do_people_love_what_they_cook = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((
                MobileBy.XPATH, "//android.view.View[@bounds='[920,1000][1006,1086]']")))
        # Choice 5: Do they like to make new things almost on a daily basis?
        self.choice_5_btn_do_they_like_to_make_new_things = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((
                MobileBy.XPATH, "//android.view.View[@bounds='[920,1226][1006,1312]']")))
        # Choice 6: Did they learn how to program on their own?
        self.choice_6_btn_do_they_learn_how_to_program_on_their_own = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((
                MobileBy.XPATH, "//android.view.View[@bounds='[920,1452][1006,1538]']")))
        # Choice 7: Do they calculate numbers faster than a calculator?
        self.choice_7_btn_do_they_calculate_numbers_faster = WebDriverWait(driver, 5).until(
            ec.visibility_of_element_located((
                MobileBy.XPATH, "//android.view.View[@bounds='[920,1678][1006,1764]']")))
        # # Main Screen 1 NEXT Button
        # self.next_btn = WebDriverWait(driver, 5).until(
        #     ec.visibility_of_element_located((MobileBy.ID, "com.promytheus.findmytalent:id/button_next")))

    def select_trait_1_emotional(self):
        self.choice_1_btn_emotional.click()

    def select_trait_2_running_jumping(self):
        self.choice_2_btn_running_jumping.click()

    def click_next_btn(self):
        action = TouchAction(self.driver)
        i = 0
        while i < 4:
            action.press(x=25, y=1750).move_to(x=25, y=300).release().perform()
            i += 1
        ele = self.driver.find_element_by_id("com.promytheus.findmytalent:id/button_next")
        ele.click()
        time.sleep(2)
