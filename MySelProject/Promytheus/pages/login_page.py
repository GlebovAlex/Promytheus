from Promytheus.locators.locators import Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.email_textbox_xpath = Locators.email_textbox_xpath
        self.password_textbox_xpath = Locators.password_textbox_xpath
        self.login_button_xpath = Locators.login_button_xpath
        self.error_message_invalid_email_or_pass = Locators.error_message_invalid_email_or_pass
        self.error_message_blank_email = Locators.error_message_blank_email
        self.error_message_blank_pass = Locators.error_message_blank_pass
        self.register_button = Locators.register_button
        self.reset_password_link = Locators.reset_password_link

    def enter_email(self, username):
        self.driver.find_element_by_xpath(self.email_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.email_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def click_login_button(self):
        ele = self.driver.find_element_by_xpath(self.login_button_xpath)
        self.driver.execute_script("arguments[0].click();", ele)

        # element = self.driver.find_element_by_xpath(self.login_button_xpath)
        # self.driver.ActionChains(self.driver).move_to_element(element).click(element).perform()

    def check_invalid_email_or_pass_error_message(self):
        msg = self.driver.find_element_by_xpath(self.error_message_invalid_email_or_pass).text
        return msg

    def check_blank_email_error_message(self):
        msg = self.driver.find_element_by_xpath(self.error_message_blank_email).text
        return msg

    def check_blank_pass_error_message(self):
        msg = self.driver.find_element_by_xpath(self.error_message_blank_pass).text
        return msg

    def click_register_button(self):
        self.driver.find_element_by_xpath(self.register_button).click()

    def click_reset_password_link(self):
        self.driver.find_element_by_xpath(self.reset_password_link).click()
