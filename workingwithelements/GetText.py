from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GetText():

    def testText(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(5)

        element = driver.find_element(By.ID, "opentab")
        print("Text on the element is " + element.text)

        driver.quit()


test = GetText()
test.testText()