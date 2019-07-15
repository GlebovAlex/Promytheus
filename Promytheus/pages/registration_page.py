
from Promytheus.locators import locators
import select


class RegisterPage():

    def __init__(self, driver):
        self.driver = driver
        self.register_btn_xpath = locators.Locators.register_btn_xpath
        self.regpage_fname_xpath = locators.Locators.regpage_fname_xpath
        self.regpage_lname_xpath = locators.Locators.regpage_lname_xpath
        self.regpage_email_xpath = locators.Locators.regpage_email_xpath
        self.regpage_phone_xpath = locators.Locators.regpage_phone_xpath
        self.regpage_pwd_xpath = locators.Locators.regpage_pwd_xpath
        self.regpage_retypepwd_xpath = locators.Locators.regpage_retypepwd_xpath
        self.regpage_country_xpath = locators.Locators.regpage_country_xpath
        self.regpage_state_xpath = locators.Locators.regpage_state_xpath
        self.regpage_city_xpath = locators.Locators.regpage_city_xpath
        self.regpage_address_xpath = locators.Locators.regpage_address_xpath
        self.regpage_zipcode_xpath = locators.Locators.regpage_zipcode_xpath
        self.regpage_createbtn_xpath = locators.Locators.regpage_createbtn_xpath
        self.regpage_pvtcheck_xpath = locators.Locators.regpage_pvtcheck_xpath
        self.regpage_okbtn_aftcreate_xpath = locators.Locators.regpage_okbtn_aftcreate_xpath
        self.regpage_exixting_emailid_errormsg_xpath = locators.Locators.regpage_exixting_emailid_errormsg_xpath

    def click_register(self):
        ele = self.driver.find_element_by_xpath(self.register_btn_xpath)
        self.driver.execute_script("arguments[0].click();", ele)

    def reg_name(self,fname,lastname):
        self.driver.find_element_by_xpath(self.regpage_fname_xpath).clear()
        self.driver.find_element_by_xpath(self.regpage_fname_xpath).send_keys(fname)
        self.driver.find_element_by_xpath(self.regpage_lname_xpath).clear()
        self.driver.find_element_by_xpath(self.regpage_lname_xpath).send_keys(lastname)

    def reg_email(self,email):
        self.driver.find_element_by_xpath(self.regpage_email_xpath).clear()
        self.driver.find_element_by_xpath(self.regpage_email_xpath).send_keys(email)

    def reg_phone(self, phone):
        self.driver.find_element_by_xpath(self.regpage_phone_xpath).clear()
        self.driver.find_element_by_xpath(self.regpage_phone_xpath).send_keys(phone)

    def reg_pwd(self,pwd):
        self.driver.find_element_by_xpath(self.regpage_pwd_xpath).clear()
        self.driver.find_element_by_xpath(self.regpage_pwd_xpath).send_keys(pwd)

        self.driver.find_element_by_xpath(self.regpage_retypepwd_xpath).clear()
        self.driver.find_element_by_xpath(self.regpage_retypepwd_xpath).send_keys(pwd)

    def reg_country(self, state, city):
        #self.driver.find_element_by_xpath(self.regpage_country_xpath)
        #self.driver.find_element_by_xpath(self.regpage_country_xpath).send_keys(country)
        #mySelect = select(self.driver.find_element_by_xpath("//i[@class='caret pull-right']"))
        #mySelect.select_by_visible_text("Austria")

        self.driver.find_element_by_xpath(self.regpage_state_xpath).clear()
        self.driver.find_element_by_xpath(self.regpage_state_xpath).send_keys(state)

        self.driver.find_element_by_xpath(self.regpage_city_xpath).clear()
        self.driver.find_element_by_xpath(self.regpage_city_xpath).send_keys(city)

    def reg_address(self, address):
        self.driver.find_element_by_xpath(self.regpage_address_xpath).clear()
        self.driver.find_element_by_xpath(self.regpage_address_xpath).send_keys(address)

    def reg_postal(self, postalcode):
         self.driver.find_element_by_xpath(self.regpage_zipcode_xpath).clear()
         self.driver.find_element_by_xpath(self.regpage_zipcode_xpath).send_keys(postalcode)

    def reg_clicksubmit(self):
        ele1 = self.driver.find_element_by_xpath(self.regpage_pvtcheck_xpath)
        self.driver.execute_script("arguments[0].click();", ele1)

        self.driver.find_element_by_xpath(self.regpage_createbtn_xpath).click()

    def reg_clickokbtn_success_reg(self):
        self.driver.find_element_by_xpath(self.regpage_okbtn_aftcreate_xpath).click()

    def check_exixting_emailid(self):
         msg = self.driver.find_element_by_xpath(self.regpage_exixting_emailid_errormsg_xpath).text
         return msg
