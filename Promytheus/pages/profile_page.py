from locators.locators import Locators


class MyProfilePage:

    def __init__(self, driver):
        self.driver = driver

        # ----------------------------------- Elements -----------------------------------

        # Password Change tab
        self.my_profile_tab_link_xpath = Locators.my_profile_link_xpath
        self.pass_change_tab_link_xpath = Locators.pass_change_tab_link_xpath
        self.current_pass_textbox_xpath = Locators.current_pass_textbox_xpath
        self.new_pass_textbox_xpath = Locators.new_pass_textbox_xpath
        self.confirm_new_pass_textbox_xpath = Locators.confirm_new_pass_textbox_xpath
        self.pass_update_btn_xpath = Locators.pass_update_btn_xpath
        self.pass_change_confirm_msg_xpath = Locators.pass_change_confirm_msg_xpath
        self.pass_change_confirm_ok_btn_xpath = Locators.pass_change_confirm_ok_btn_xpath
        self.p_user_icon_link_xpath = Locators.p_user_icon_link_xpath
        self.p_sign_out_link_xpath = Locators.p_sign_out_link_xpath

        # ----------------------------------- Methods -----------------------------------

        # My Profile tab

    # Password Change tab methods
    def click_pass_change_tab_link(self):
        self.driver.find_element_by_xpath(self.pass_change_tab_link_xpath).click()

    def enter_current_password(self, email):
        self.driver.find_element_by_xpath(self.current_pass_textbox_xpath).send_keys(email)

    def enter_new_password(self, password):
        self.driver.find_element_by_xpath(self.new_pass_textbox_xpath).send_keys(password)

    def enter_confirm_password(self, password):
        self.driver.find_element_by_xpath(self.confirm_new_pass_textbox_xpath).send_keys(password)

    def click_update_button(self):

        ele = self.driver.find_element_by_xpath(self.pass_update_btn_xpath)
        self.driver.execute_script("arguments[0].click();", ele)

        # self.driver.find_element_by_xpath(self.pass_update_btn_xpath).click()

    def confirm_update_pass_message(self):
        msg = self.driver.find_element_by_xpath(self.pass_change_confirm_msg_xpath).text
        return msg

    def click_confirm_popup_ok_button(self):
        ele = self.driver.find_element_by_xpath(self.pass_change_confirm_msg_xpath)
        self.driver.execute_script("arguments[0].click();", ele)

    def click_p_user_icon(self):
        ele = self.driver.find_element_by_xpath(self.p_user_icon_link_xpath)
        self.driver.execute_script("arguments[0].click();", ele)

    def click_p_sign_out(self):
        ele = self.driver.find_element_by_xpath(self.p_sign_out_link_xpath)
        self.driver.execute_script("arguments[0].click();", ele)
