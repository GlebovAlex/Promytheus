from selenium import webdriver
import time
import unittest
from Promytheus.pages.personalitytraits_page import p_traits
from Promytheus.pages.login_page import LoginPage


class Personality(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path= "/Users/jeevanbyappareddy/PycharmProjects/QABootCampProjects/driver/chromedriver")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()

    def test_ptraits(self):

        driver = self.driver
        driver.get("https://app.promytheus.net")



        #directly editing a recordfrom the home page

        #clicking on the check box of the record
        # login_edit_xpath = "//tr[1]//td[1]//div[1]//label[1]//input[1]"
        # self.driver.find_element_by_xpath(login_edit_xpath).click()
        # time.sleep(2)

        #clicking on the edit symbol of the record
        # self.driver.find_element_by_xpath("//tr[1]//td[9]//a[1]").click()
        # time.sleep(2)

        ptraits = p_traits(driver)
        time.sleep(2)

        #clicking on personal traits tab
        ptraits.click_traits_tab()
        time.sleep(2)

        #clicking on the check boxes in the personality traits page
        #ptraits.click_chkbx_pttab()
        #time.sleep(1)

        #click next button to navigate to story page
        ptraits.click_next_btn()
        time.sleep(5)

        ptraits.enter_age_storytab()
        time.sleep(2)



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__=='__main__':
    unittest.main()
