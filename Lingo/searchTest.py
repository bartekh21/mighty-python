from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class RunFFTest():

    def autocompleteTrigger(self, driver, phrase):
        searchInput = driver.find_element(By.XPATH,
                                          "//section[@class='HeroSection__Wrapper-sc-1c8c1ss-0 kATzpD']//input")
        searchInput.click()
        time.sleep(1)
        searchInput.click()
        for a in phrase:
            searchInput.send_keys(a)
            time.sleep(0.2)

    def testMethod(self):
        # initiate webdriver
        password = ''
        profile = webdriver.FirefoxProfile()
        profile.set_preference('network.http.phishy-userpass-length', 255)
        driver = webdriver.Firefox(firefox_profile=profile)
        driver.maximize_window()
        driver.get("https://staging:" + password + "@lvt.staging.devguru.co/")
        driver.implicitly_wait(5)

        # open the URL once again to deal with auth problem
        driver.get("https://lvt.staging.devguru.co/")

        # URL definition for comparision
        spanishSearchURL = "https://lvt.staging.devguru.co/suchergebnisse?sprache[]=0"

        # send phrase to search input
        self.autocompleteTrigger(driver, "spanish")

        # click first position in dropdown
        spanishFirstItem = driver.find_element(By.ID, "downshift-0-item-0")
        time.sleep(1)
        spanishFirstItem.click()
        time.sleep(5)

        # compare search results URL
        if driver.current_url == spanishSearchURL:
            print("Search results pages URL matches the spanish search results URL")
        else:
            print("URLs don't match")

        driver.quit()


ff = RunFFTest()
ff.testMethod()
