from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class HiddenElements():

    def testPracticePage(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        textBox = driver.find_element(By.ID, "displayed-text")
        print("Text is visible? " + str(textBox.is_displayed()))  # exception if not present in the DOM

        # click hide butotn
        driver.find_element(By.ID, "hide-textbox").click()

        # print the state of checkbox
        print("Text is visible? " + str(textBox.is_displayed()))  # exception if not present in the DOM

        # click show button
        driver.find_element(By.ID, "show-textbox").click()

        # print the state of checkbox
        print("Text is visible? " + str(textBox.is_displayed()))  # exception if not present in the DOM

        driver.quit()

    def textExpediaPage(self):
        baseURL = "https://www.expedia.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[@data-gcw-component='gcw-traveler-amount-select']").click()
        time.sleep(2)

        childAgeBtn = driver.find_element(By.ID, "flight-age-select-1-label-hp-flight")
        print("Child age button is visible? " + str(childAgeBtn.is_displayed())) # exception if not present in the DOM

        driver.find_element(
            By.XPATH, "//div[@class='children-wrapper']//button[@class='uitk-step-input-button uitk-step-input-plus']").click()
        time.sleep(2)

        childAgeBtn = driver.find_element(By.ID, "flight-age-select-1-label-hp-flight")
        print("Child age button is visible? " + str(childAgeBtn.is_displayed()))  # exception if not present in the DOM

        driver.quit()


test = HiddenElements()
test.testPracticePage()

test.textExpediaPage()