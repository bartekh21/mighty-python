from selenium import webdriver

class FindByLinkText():

    def testMethod(self):
        driver = webdriver.Firefox()
        baseUrl = "https://learn.letskodeit.com/p/practice"

        driver.get(baseUrl)
        elementByLinkText = driver.find_element_by_link_text("Login")

        if elementByLinkText is not None:
            print ("We found an element by link text!")

        elementByPartialLinkText = driver.find_element_by_partial_link_text("Pract")

        if elementByPartialLinkText is not None:
            print ("We found an element by partial link text!")

        driver.quit()


ff = FindByLinkText()
ff.testMethod()