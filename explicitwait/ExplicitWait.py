from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from ExplicitWaitTypes import ExplicitWaitType


class ExplicitWaitDemo():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.implicitly_wait(.5)
        wait = ExplicitWaitType(driver)
        driver.maximize_window()
        driver.get(baseURL)

        element = wait.waitForElement("bmwcheck")
        element.click()

        driver.quit()


ff = ExplicitWaitDemo()
ff.test()