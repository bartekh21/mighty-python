from selenium import webdriver

class FindById():

    def testMethod(self):
        driver = webdriver.Firefox()
        baseUrl = "https://learn.letskodeit.com/p/practice"

        driver.get(baseUrl)
        elementById = driver.find_element_by_id("name")

        if elementById is not None:
            print ("We found an element by ID!")

        elementByName = driver.find_element_by_name("show-hide")

        if elementByName is not None:
            print ("We found an element by name!")

        driver.quit()


ff = FindById()
ff.testMethod()