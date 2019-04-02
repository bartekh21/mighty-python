from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ValueOfElementAttribute():

    def testValue(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        element = driver.find_element(By.ID, "name")
        print("Value of the attribute is " + element.get_attribute("class"))

        driver.quit()


test = ValueOfElementAttribute()
test.testValue()