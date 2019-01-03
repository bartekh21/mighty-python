from selenium import webdriver
from selenium.webdriver.common.by import By

class FindListOfElements():

    def testMethod(self):
        driver = webdriver.Firefox()
        baseUrl = "https://learn.letskodeit.com/p/practice"

        driver.get(baseUrl)
        elementListByClassName = driver.find_element_by_class_name("inputs")

        if elementListByClassName is not None:
            print ("We found it!")

        elementListByTagName = driver.find_elements(By.TAG_NAME, "h1")

        if elementListByTagName is not None:
            print ("We found it!")

        driver.quit()


ff = FindListOfElements()
ff.testMethod()