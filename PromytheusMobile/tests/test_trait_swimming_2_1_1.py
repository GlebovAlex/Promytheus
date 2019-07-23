from appium import webdriver
import time
import unittest
from pages.main_screen import MainScreen
from pages.choice_2_running_screens.trait_2_running_path_2 import RunningJumpingScreen
from pages.choice_2_running_screens.trait_2_running_path_2_1 import RunningJumpingScreen2
from pages.choice_2_running_screens.trait_2_running_path_2_1_1 import RunningJumpingScreen3


class TestProm(unittest.TestCase):

    def setUp(self):
        desired_capabilities = {
            "platformName": "Android",
            "deviceName": "Pixel 2 Android Emulator",
            "udid": "emulator-5554",
            "appPackage": "com.promytheus.findmytalent",
            "appWaitActivity": "com.promytheus.findmytalent.MainActivity",
            "appActivity": "com.promytheus.findmytalent.SplashActivity",
            "app": "C:/Users/jolee/Downloads/findmytalent-prod app-release.apk"
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
        time.sleep(8)
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
