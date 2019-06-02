from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToFrame():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        alertButton = driver.find_element(By.ID, "alertbtn")
        confirmButton = driver.find_element(By.ID, "confirmbtn")

        driver.find_element(By.ID, "name").send_keys("Bartek")

        alertButton.click()
        time.sleep(2)
        alertPopup = driver.switch_to.alert
        alertPopup.accept()
        time.sleep(2)

        driver.find_element(By.ID, "name").send_keys("Bartek")
        confirmButton.click()
        time.sleep(2)
        confirmPopup = driver.switch_to.alert
        confirmPopup.dismiss()
        time.sleep(2)

        driver.quit()


ff = SwitchToFrame()
ff.test()
