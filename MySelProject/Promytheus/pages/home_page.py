from Promytheus.locators.locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.user_icon_link_xpath = Locators.user_icon_link_xpath
        self.sign_out_link_xpath = Locators.sign_out_link_xpath

    def click_user_icon(self):
        self.driver.find_element_by_xpath(self.user_icon_link_xpath).click()

    def click_sign_out(self):
        self.driver.find_element_by_xpath(self.sign_out_link_xpath).click()
