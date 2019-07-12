from locators.locators import Locators


class TalentsForm:

    def __init__(self, driver):
        self.driver = driver

        # ----------------------------------- Elements -----------------------------------

        self.category_select_xpath = Locators.category_select_xpath
        self.category_business_xpath = Locators.category_business_xpath

        # Next button
        self.next_btn = Locators.next_btn

        # Previous button
        self.prev_btn = Locators.prev_btn

        # ----------------------------------- Methods -----------------------------------

    def click_next_btn(self):
        ele = self.driver.find_element_by_xpath(self.next_btn)
        self.driver.execute_script("arguments[0].click();", ele)

    def click_previous_btn(self):
        ele = self.driver.find_element_by_xpath(self.prev_btn).click()
        self.driver.execute_script("arguments[0].click();", ele)

    def click_category_field(self):
        self.driver.find_element_by_xpath(self.category_select_xpath).click()

    def click_category_business(self):
        self.driver.find_element_by_xpath(self.category_business_xpath).click()

