from appium import webdriver
import time
import unittest
from PromytheusMobile.pages.main_screen import MainScreen


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

    def test_01_select_trait_psychic_path_1(self):
        main = MainScreen(self.driver)
        main.select_trait_1_emotional()
        main.click_next_btn()
        result = self.driver.find_element_by_id("com.promytheus.findmytalent:id/category_name_text").text
        self.assertEqual(result, "Psychic/Intuitive/Predictive")
        time.sleep(4)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestProm)
    unittest.TextTestRunner(verbosity=2).run(suite)
