#!/usr/bin/python3
import json
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import time

appURL = "https://app.promytheus.net/sign-in.html"


class LoginUser(unittest.TestCase):
    def setUp(self):
        #     # global options
        #     # options = Options()
        #     # options.headless = True
        #     # options.add_argument('--no-sandbox')
        #     # options.add_argument('--disable-dev-shm-usage')
        #     # options.binary_location = 'usr/bin/google-chrome'
        self.driver = webdriver.Chrome(
            executable_path='C:/Users/jolee/Desktop/Selenium/Promytheus/drivers/chromedriver.exe')
        # driver = webdriver.Chrome(executable_path='chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get(appURL)

    def test_login(self):
        driver = self.driver
        with open('C:/Users/jolee/Desktop/Selenium/Promytheus/testdata/test_data.json') as test_data:
            data = json.loads(test_data.read())
            # try:
            driver.maximize_window()
            driver.get(appURL)
            WebDriverWait(driver, 10).until(
                lambda driver: driver.find_element_by_xpath("//input[@name='email']")).send_keys(
                data["login_test_data"]["user_1"]["email"])
            WebDriverWait(driver, 10).until(
                lambda driver: driver.find_element_by_xpath("//input[@name='password']")).send_keys(
                data["login_test_data"]["user_1"]["password"])
            driver.find_element_by_xpath("//button[@id='login']").click()
            title = driver.title
            print(title)
            # except Exception as e:
            #     print("Login not successful due to error " + str(e))

    def tearDown(self):
        print("----------End of Login Test script----------")
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
