from locators import locators

class p_traits():
    def __init__(self,driver):
        self.driver = driver
        self.pt_personality_tab_xpath = locators.Locators.pt_personality_tab_xpath
        self.pt_checkbox1_xpath = locators.Locators.pt_checkbox1_xpath
        self.pt_checkbox6_xpath = locators.Locators.pt_checkbox6_xpath
        self.pt_nextbtn_xpath = locators.Locators.pt_nextbtn_xpath
        self.stry_age_xpath = locators.Locators.stry_age_xpath
        self.stry_interest_level_xpath = locators.Locators.stry_interest_level_xpath
        self.stry_interest_menusel_xpath = locators.Locators.stry_interest_menusel_xpath
        self.stry_nextbtn_xpath = locators.Locators.stry_nextbtn_xpath

    def click_traits_tab(self):
        self.driver.find_element_by_xpath(self.pt_personality_tab_xpath).click()

    def click_chkbx_pttab(self):
        #self.driver.find_element_by_xpath(self.pt_checkbox1_xpath).click()
        self.driver.find_element_by_xpath(self.pt_checkbox6_xpath).click()

    def click_next_btn(self):
        self.driver.find_element_by_xpath(self.pt_nextbtn_xpath).click()

    #funtions to perform on story tab
    def enter_age_storytab(self):
        self.driver.find_element_by_xpath(self.stry_age_xpath).send_keys("9")
        self.driver.find_element_by_xpath(self.stry_interest_level_xpath).click()
        self.driver.find_element_by_xpath(self.stry_interest_menusel_xpath).click()


    def click_next_button_storytab(self):
        self.driver.find_element_by_xpath(self.stry_nextbtn_xpath).click()
