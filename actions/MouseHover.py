from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class MouseHover():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)

        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(2)

        element = driver.find_element(By.ID, "mousehover")
        itemToClick = driver.find_element(By.XPATH, "//div[@class='mouse-hover-content']//a[text()='Top']")

        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse hovered on element")
            time.sleep(2)
            itemToClick.click()
            print("Item clicked")
        except:
            print("Mouse hover failed")

        driver.quit()


ff = MouseHover()
ff.test()