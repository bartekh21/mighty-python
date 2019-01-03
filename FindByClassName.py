from selenium import webdriver

class FindByClassName():

    def testMethod(self):
        driver = webdriver.Firefox()
        baseUrl = "https://learn.letskodeit.com/p/practice"

        driver.get(baseUrl)
        elementByClassName = driver.find_element_by_class_name("displayed-class")
        elementByClassName.send_keys("Testing The Element")

        if elementByClassName is not None:
            print ("We found an element by class name!")

        elementByTagName = driver.find_element_by_tag_name("h1")
        text = elementByTagName.text

        if elementByTagName is not None:
            print ("We found an element by tag name and the text on element is: " + text)

        driver.quit()


ff = FindByClassName()
ff.testMethod()