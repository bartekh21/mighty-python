from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class WorkingWithDropdownElement():

    @staticmethod
    def dropdownTest():
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        dropdown = driver.find_element(By.XPATH, "//select[@id = 'carselect']")
        sel = Select(dropdown)

        sel.select_by_value("benz")
        print("Select Benz by value")
        time.sleep(2)

        sel.select_by_index("2")
        print("Select Honda by index")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print("Select BMW by visible text")
        time.sleep(2)

        sel.select_by_index(2)
        print("Select Honda by index")
        time.sleep(2)

        driver.quit()


WorkingWithDropdownElement.dropdownTest()