from appium import webdriver
import time
import unittest
from PromytheusMobile.pages.main_screen import MainScreen


class TestProm(unittest.TestCase):

    def setUp(self):
        userName = "joanlee1"
        accessKey = "QJ3u2m7G7iqF7U7sqEit"
        desired_capabilities = {
            "name": "Promytheus Mobile Test: test_tait_psychic_1.py",
            "platformName": "Android",
            "deviceName": "Pixel 2 Android Emulator",
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
