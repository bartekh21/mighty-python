from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():

    def testMethod(self):
        #initiate webdriver
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()

        # go to url
        driver.get(baseURL)
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        loginLink.click()

        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test")

        passwordField = driver.find_element(By.ID ,"user_password")
        passwordField.send_keys("test")

        time.sleep(3)
        passwordField.clear()

        time.sleep(3)
        passwordField.send_keys("test")

        driver.quit()


ff = ClickAndSendKeys()
ff.testMethod()