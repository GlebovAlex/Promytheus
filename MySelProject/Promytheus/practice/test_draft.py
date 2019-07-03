from selenium import webdriver
from Promytheus.browsers.browser import Browser
import time


b = Browser()
driver = webdriver.Firefox(executable_path=b.firefox)
driver.maximize_window()
driver.implicitly_wait(20)

# Navigate to web page
driver.get("https://app.promytheus.net")

# Verify expected error message
driver.find_element_by_xpath("//input[@name='email']").send_keys("jolee.test123@gmail.com")

#driver.find_element_by_xpath("//input[@name='password']").send_keys("password")

time.sleep(3)

ele = driver.find_element_by_xpath("//button[@id='login']")
driver.execute_script("arguments[0].click();", ele)

driver.find_element_by_xpath("//button[@id='login']").click()

msg = driver.find_element_by_xpath("//input[@name='password']/parent::div/span[2]").text

print(msg)

driver.quit()



