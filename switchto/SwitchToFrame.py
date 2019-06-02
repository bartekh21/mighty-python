from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToFrame():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.execute_script("window.scrollBy(0, 1000);")

        driver.switch_to.frame(0)
        time.sleep(2)

        searchBox = driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("python")
        time.sleep(2)

        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("test successful")
        time.sleep(2)

        driver.quit()


ff = SwitchToFrame()
ff.test()
