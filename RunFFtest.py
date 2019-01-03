from selenium import webdriver

class RunFFTest():

    def testMethod(self):
        #initiate webdriver
        driver = webdriver.Firefox()

        # go to url
        driver.get("http://www.letskodeit.com")
        driver.quit()


ff = RunFFTest()
ff.testMethod()