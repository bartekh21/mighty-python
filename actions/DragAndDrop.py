from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class DragAndDrop():

    def test(self):
        baseURL = "https://jqueryui.com/droppable/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(3)

        driver.switch_to.frame(0)
        dragElement = driver.find_element(By.ID, "draggable")
        dropElement = driver.find_element(By.ID, "droppable")

        try:
            actions = ActionChains(driver)
            actions.drag_and_drop(dragElement, dropElement).perform()
            print("Drag and drop successful")
            time.sleep(2)
        except:
            print("Drag and drop failed")

        driver.quit()


ff = DragAndDrop()
ff.test()