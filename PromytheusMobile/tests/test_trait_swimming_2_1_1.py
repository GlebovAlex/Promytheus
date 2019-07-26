#!/usr/bin/python3
from appium import webdriver
import time
import unittest
from PromytheusMobile.pages.main_screen import MainScreen
from PromytheusMobile.pages.choice_2_running_screens.trait_2_running_path_2 import RunningJumpingScreen
from PromytheusMobile.pages.choice_2_running_screens.trait_2_running_path_2_1 import RunningJumpingScreen2


class TestProm(unittest.TestCase):

    def setUp(self):

        userName = "joanlee1"
        accessKey = "QJ3u2m7G7iqF7U7sqEit"
        desired_capabilities = {
            "name": "Promytheus Mobile Test: test_tait_swimming_2_1_1.py",
            "platformName": "Android",
            "deviceName": "Pixel Android Emulator",
            "device": "Google Pixel",
            "browserstack.appium_version": "1.13.0",
            "os": "android",
            "os_version": "7.1",
            "appPackage": "com.promytheus.findmytalent",
            "appWaitActivity": "com.promytheus.findmytalent.MainActivity",
            "appActivity": "com.promytheus.findmytalent.SplashActivity",
            "app": "bs://48ec8a4ad46f4396e1ec613ed61e8529e55851e1"
        }
        self.driver = webdriver.Remote("http://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_capabilities)
        time.sleep(3)
        desired_capabilities["appActivity"] = "com.promytheus.findmytalent.MainActivity"

    def test_02_trait_swimming_path_2_1_1(self):
        main = MainScreen(self.driver)
        main.select_trait_2_running_jumping()
        main.click_next_btn()

        running = RunningJumpingScreen(self.driver)
        running.select_choice_1_prefer_own_company()
        running.click_next_btn()

        running_2 = RunningJumpingScreen2(self.driver)
        running_2.select_choice_1_swims()
        running_2.click_next_btn()

        time.sleep(3)
        result = self.driver.find_element_by_id("com.promytheus.findmytalent:id/category_name_text").text
        self.assertEqual(result, "Swimming (1.1.1.2)")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestProm)
    unittest.TextTestRunner(verbosity=2).run(suite)
