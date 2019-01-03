from selenium import webdriver
import os

class RunChromeTest():

    def testMethod(self):
        #initiate webdriver
        driver = webdriver.Chrome()

        # go to url
        driver.get("http://www.letskodeit.com")
        driver.quit()


chrome = RunChromeTest()
chrome.testMethod()