from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class RadioButtonsAndCheckboxes():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        bmwRadioBtn = driver.find_element(By.ID, "bmwradio")
        bmwRadioBtn.click()

        time.sleep(2)

        benzRadioBtn = driver.find_element(By.ID, "benzradio")
        benzRadioBtn.click()

        bmwCheckbox = driver.find_element(By.ID, "bmwcheck")
        bmwCheckbox.click()

        time.sleep(2)

        benzCheckbox = driver.find_element(By.ID, "benzcheck")
        benzCheckbox.click()

        time.sleep(2)

        print("Is BMW Radio Button selected? " + str(bmwRadioBtn.is_selected()))

        driver.quit()

gaga = RadioButtonsAndCheckboxes()
gaga.test()