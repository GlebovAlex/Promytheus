from locators.locators import Locators
import time

class TraitsPage:

    def __init__(self, driver):

        self.driver = driver

        self.first = Locators.first_question_xpath
        self.second = Locators.second_question_xpath
        self.third = Locators.third_question_xpath
        self.fourth = Locators.fourth_question_xpath
        self.fifth = Locators.fifth_question_xpath
        self.sixth = Locators.sixth_question_xpath

        self.seven = Locators.seventh_question_xpath
        self.eighth = Locators.eight_question_xpath
        self.ninth = Locators.ninth_question_xpath
        self.tenth = Locators.tenth_question_xpath
        self.eleventh = Locators.eleventh_question_xpath
        self.twelfth = Locators.twelfth_question_xpath

        self.thirteenth = Locators.thirteenth_question_xpath
        self.fourteen = Locators.fourteenth_question_xpath
        self.fifteen = Locators.fifteenth_question_xpath
        self.sixteen = Locators.sixteenth_question_xpath
        self.next = Locators.traits_next_button_xpath

    def complete_talent_trait_tab(self):
        self.driver.find_element_by_xpath(self.first).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.second).click()
        #time.sleep(2)
        self.driver.find_element_by_xpath(self.third).click()
        #self.driver.find_element_by_css_selector(self.third).click()
        # time.sleep(2)
        self.driver.find_element_by_xpath(self.fourth).click()
        #time.sleep(2)
        self.driver.find_element_by_xpath(self.fifth).click()
        #time.sleep(2)
        self.driver.find_element_by_xpath(self.sixth).click()
        #time.sleep(2)
        self.driver.find_element_by_xpath(self.seven).click()
        #time.sleep(2)
        self.driver.find_element_by_xpath(self.eighth).click()
        #time.sleep(2)
        self.driver.find_element_by_xpath(self.ninth).click()
        #time.sleep(2)
        self.driver.find_element_by_xpath(self.tenth).click()
        #time.sleep(2)
        self.driver.find_element_by_xpath(self.eleventh).click()
        #time.sleep(2)
        self.driver.find_element_by_xpath(self.twelfth).click()
        #time.sleep(2)
        self.driver.find_element_by_xpath(self.thirteenth).click()
        #time.sleep(2)
        self.driver.find_element_by_xpath(self.fourteen).click()
        #time.sleep(2)
        self.driver.find_element_by_xpath(self.fifteen).click()
        #time.sleep(2)
        self.driver.find_element_by_xpath(self.sixteen).click()
        #time.sleep(2)
        self.driver.find_element_by_xpath(self.next).click()
        time.sleep(2)




