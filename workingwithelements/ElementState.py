from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ElementState():

    def isEnabled(self):
        baseURL = "http://www.google.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)
        e1 = driver.find_element(By.CLASS_NAME, "gLFyf")

        if (e1.is_enabled()):
            e1.send_keys("letskodeit")
            print("e1 is enabled")
        else:
            print("e1 is disabled")

        driver.quit()


test = ElementState()
test.isEnabled()