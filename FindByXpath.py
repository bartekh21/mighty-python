from selenium import webdriver

class FindByXpath():

    def testMethod(self):
        driver = webdriver.Firefox()
        baseUrl = "https://learn.letskodeit.com/p/practice"

        driver.get(baseUrl)
        elementByXpath = driver.find_element_by_xpath("//*[@id='name']")

        if elementByXpath is not None:
            print ("We found an element by XPATH!")

        elementByCSS = driver.find_element_by_css_selector("#displayed-text")

        if elementByCSS is not None:
            print ("We found an element by CSS!")

        driver.quit()


ff = FindByXpath()
ff.testMethod()