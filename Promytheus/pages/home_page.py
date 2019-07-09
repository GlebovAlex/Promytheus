from locators.locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.user_icon_link_xpath = Locators.user_icon_link_xpath
        self.my_profile_link_xpath = Locators.my_profile_link_xpath
        self.sign_out_link_xpath = Locators.sign_out_link_xpath
        self.home_icon_xpath = Locators.home_icon_xpath

    def click_home_icon(self):
        ele = self.driver.find_element_by_xpath(self.home_icon_xpath)
        self.driver.execute_script("arguments[0].click();", ele)

    def click_user_icon(self):
        ele = self.driver.find_element_by_xpath(self.user_icon_link_xpath)
        self.driver.execute_script("arguments[0].click();", ele)

    def click_my_profile_link(self):
        self.driver.find_element_by_xpath(self.my_profile_link_xpath).click()

    def click_sign_out(self):
        self.driver.find_element_by_xpath(self.sign_out_link_xpath).click()
