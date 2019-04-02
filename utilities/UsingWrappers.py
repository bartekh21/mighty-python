from selenium import webdriver
from selenium.webdriver.common.by import By
from HandyWrappers import HandyWrapper
import time


class UsingWrappers():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
        hw = HandyWrapper(driver)

        driver.get(baseURL)

        element = hw.getElement("opentab", "ID")
        print(element.text)

        driver.quit()


ff = UsingWrappers()
ff.test()