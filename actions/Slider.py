from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class DragAndDrop():

    def test(self):
        baseURL = "https://jqueryui.com/slider/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        driver.switch_to.frame(0)
        slider = driver.find_element(By.XPATH, "//div[@id='slider']//span")

        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(slider, 200, 0).perform()
            print("Slide successful")
            time.sleep(2)
        except:
            print("Slide failed")

        driver.quit()


ff = DragAndDrop()
ff.test()