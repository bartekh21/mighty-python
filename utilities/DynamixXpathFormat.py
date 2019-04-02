from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DynamicXpathFormat():

    def test(self):
        baseURL = "https://www.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)

        # log in
        driver.find_element(By.ID, "comp-iiqg1vggactionTitle").click()
        driver.find_element(By.ID, "signUpDialogswitchDialogLink").click()
        time.sleep(1)
        email = driver.find_element(By.ID, "memberLoginDialogemailInputinput")
        email.send_keys("test123@example.com")
        password = driver.find_element(By.ID, "memberLoginDialogpasswordInputinput")
        password.send_keys("abcabc")
        driver.find_element(By.ID, "memberLoginDialogokButton").click()
        time.sleep(5)

        # go to courses page
        driver.find_element(By.ID, "DrpDwnMn01label").click()

        # select course
        course = "//div[contains(@class,'item')]//div//h3[contains(text(),'{0}')]"
        course2 = "//div[@class='item']//h3[@title='JavaScript - A Complete Guide']"
        courseLocator = course.format("JavaScript - A Complete Guide")
        driver.find_element(By.XPATH, course2).click()
        time.sleep(2)

        driver.quit()


ff = DynamicXpathFormat()
ff.test()