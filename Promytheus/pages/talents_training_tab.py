from locators.locators import Locators


class TalentsTraining:

    def __init__(self, driver):
        self.driver = driver

        # ----------------------------------- Elements -----------------------------------

        # Training tab link
        self.training_tab_link_xpath = Locators.training_tab_link_xpath

        # Testimonies of people who know talent
        self.training_history_select_xpath = Locators.training_history_select_xpath
        self.training_history_select_none_xpath = Locators.training_history_select_none_xpath
        self.training_history_select_less_one_year_xpath = Locators.training_history_select_less_one_year_xpath
        self.training_history_select_more_one_year_xpath = Locators.training_history_select_more_one_year_xpath
        self.training_history_select_more_two_year_xpath = Locators.training_history_select_more_two_year_xpath
        self.training_history_select_more_three_year_xpath = Locators.training_history_select_more_three_year_xpath
        self.training_history_select_more_five_year_xpath = Locators.training_history_select_more_five_year_xpath

        # Professionally Coached
        self.coached_radio_yes_xpath = Locators.coached_radio_yes_xpath
        self.coached_radio_no_xpath = Locators.coached_radio_no_xpath
        self.coached_enter_name_textbox_xpath = Locators.coached_enter_name_textbox_xpath
        self.coached_enter_success_level_xpath = Locators.coached_enter_success_level_xpath

        # Types of Training
        self.training_type_intensive_xpath = Locators.training_type_intensive_xpath
        self.training_type_sometimes_xpath = Locators.training_type_sometimes_xpath

        # School or College
        self.school_textbox_xpath = Locators.school_textbox_xpath

        # Success Level
        self.school_success_level_textbox_xpath = Locators.school_success_level_textbox_xpath

        # Skill Level
        self.skill_level_radio_beginner_xpath = Locators.skill_level_radio_beginner_xpath
        self.skill_level_radio_advanced_xpath = Locators.skill_level_radio_advanced_xpath
        self.skill_level_radio_pro_xpath = Locators.skill_level_radio_pro_xpath

        # Next button
        self.training_button_next_xpath = Locators.training_button_next_xpath

        # Previous button
        self.training_button_previous_xpath = Locators.training_button_previous_xpath

        # ----------------------------------- Methods -----------------------------------

    def click_training_tab_link(self):
        self.driver.find_element_by_xpath(self.training_tab_link_xpath).click()

    def click_prof_coached_yes(self):
        self.driver.find_element_by_xpath(self.coached_radio_yes_xpath).click()

    def click_prof_coached_no(self):
        self.driver.find_element_by_xpath(self.coached_radio_no_xpath).click()

    def enter_name_coached_field(self, text):
        self.driver.find_element_by_xpath(self.coached_enter_name_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.coached_enter_name_textbox_xpath).send_keys(text)

    def enter_success_level_coached_field(self, text):
        self.driver.find_element_by_xpath(self.coached_enter_success_level_xpath).clear()
        self.driver.find_element_by_xpath(self.coached_enter_success_level_xpath).send_keys(text)

    def click_training_type_intensive(self):
        self.driver.find_element_by_xpath(self.training_type_intensive_xpath).click()

    def click_training_type_sometimes(self):
        self.driver.find_element_by_xpath(self.training_type_sometimes_xpath).click()

    def enter_school_field(self, text):
        self.driver.find_element_by_xpath(self.school_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.school_textbox_xpath).send_keys(text)

    def enter_success_level_field(self, text):
        self.driver.find_element_by_xpath(self.school_success_level_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.school_success_level_textbox_xpath).send_keys(text)

    def click_beginner_skill_level_radio(self):
        self.driver.find_element_by_xpath(self.skill_level_radio_beginner_xpath).click()

    def click_advanced_skill_level_radio(self):
        self.driver.find_element_by_xpath(self.skill_level_radio_advanced_xpath).click()

    def click_pro_skill_level_radio(self):
        self.driver.find_element_by_xpath(self.skill_level_radio_pro_xpath).click()




