from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElementsList():

    def testMethod(self):

        driver = webdriver.Firefox()
        baseURL = "https://learn.letskodeit.com/p/practice"

        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        checkboxes = driver.find_elements(By.XPATH, "//input[contains(@type, 'checkbox') and contains(@name, 'cars')]")
        size = len(checkboxes)
        print("Size of a list = " + str(size))

        for a in checkboxes:
            isSelected = a.is_selected()
            if not isSelected:
                a.click()

        driver.quit()


test = WorkingWithElementsList()
test.testMethod()