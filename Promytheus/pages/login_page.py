from locators.locators import Locators
import json
import time


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        # ----------------------------------- Elements -----------------------------------

        self.email_textbox_xpath = Locators.email_textbox_xpath
        self.pass_textbox_xpath = Locators.pass_textbox_xpath
        self.login_btn_xpath = Locators.login_btn_xpath
        self.error_msg_login_xpath = Locators.error_msg_login_xpath
        self.error_msg_blank_email_xpath = Locators.error_msg_blank_email_xpath
        self.error_msg_blank_pass_xpath = Locators.error_msg_blank_pass_xpath
        self.register_btn_xpath = Locators.register_btn_xpath
        self.reset_pass_link_xpath = Locators.reset_pass_link_xpath

        # ----------------------------------- Methods -----------------------------------

    def enter_email(self, username):
        self.driver.find_element_by_xpath(self.email_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.email_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.pass_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.pass_textbox_xpath).send_keys(password)

    def click_login_button(self):
        ele = self.driver.find_element_by_xpath(self.login_btn_xpath)
        self.driver.execute_script("arguments[0].click();", ele)

        # element = self.driver.find_element_by_xpath(self.login_button_xpath)
        # self.driver.ActionChains(self.driver).move_to_element(element).click(element).perform()

    def check_invalid_user_error_message(self):
        msg = self.driver.find_element_by_xpath(self.error_msg_login_xpath).text
        return msg

    def check_blank_email_error_message(self):
        msg = self.driver.find_element_by_xpath(self.error_msg_blank_email_xpath).text
        return msg

    def check_blank_pass_error_message(self):
        msg = self.driver.find_element_by_xpath(self.error_msg_blank_pass_xpath).text
        return msg

    def check_unconfirmed_email_error_message(self):
        msg = self.driver.find_element_by_xpath(self.error_msg_login_xpath).text
        return msg

    def click_register_button(self):
        ele = self.driver.find_element_by_xpath(self.register_btn_xpath)
        self.driver.execute_script("arguments[0].click();", ele)

    def click_reset_password_link(self):
        self.driver.find_element_by_xpath(self.reset_pass_link_xpath).click()

    def login(self):
        with open('C:/Users/jolee/Desktop/Selenium/Promytheus/testdata/test_data.json', encoding='utf-8') as test_data:
            data = json.loads(test_data.read())
        self.driver.find_element_by_xpath(self.email_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.email_textbox_xpath).send_keys(data['login_test_data']['user_1']['email'])
        self.driver.find_element_by_xpath(self.pass_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.pass_textbox_xpath).send_keys(data['login_test_data']['user_1']['password'])
        time.sleep(2)
        ele = self.driver.find_element_by_xpath(self.login_btn_xpath)
        self.driver.execute_script("arguments[0].click();", ele)
