from selenium import webdriver
from selenium.webdriver.common.by import By
from HandyWrappers import HandyWrapper
import time


class ElementPresentTest():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        hw = HandyWrapper(driver)
        driver.get(baseURL)

        elementResult = hw.isElementPresent("name", By.ID)
        print(str(elementResult))

        elementResult2 = hw.elementPresenceCheck("//input[@id='name1']", By.XPATH)
        print(str(elementResult2))

        driver.quit()


ff = ElementPresentTest()
ff.test()