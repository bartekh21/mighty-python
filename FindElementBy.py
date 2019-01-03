from selenium import webdriver
from selenium.webdriver.common.by import By

class FindById():

    def testMethod(self):
        driver = webdriver.Firefox()
        baseUrl = "https://learn.letskodeit.com/p/practice"

        driver.get(baseUrl)
        elementById = driver.find_element(By.ID, "name")
        if elementById is not None:
            print ("We found an element by ID!")

        driver.quit()


ff = FindById()
ff.testMethod()