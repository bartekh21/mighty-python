from selenium import webdriver

class BrowserInteraction():

    def testMethod(self):
        #initiate webdriver
        driver = webdriver.Firefox()
        baseURL = "https://learn.letskodeit.com/p/practice"

        # window maximize
        driver.maximize_window()

        # open the url
        driver.get(baseURL)

        # get title
        pageTitle = driver.title
        print(pageTitle)

        # get current url
        currentUrl = driver.current_url
        print(currentUrl)

        # browser refresh
        driver.refresh()
        print("Browser refreshed for the first time")
        driver.get(baseURL)
        print("Browser refreshed for the second time")

        # open another url
        driver.get("http://google.com")

        # browser back
        driver.back()
        print("One step back in browser history")

        # browser forward
        driver.forward()
        print("One step forward in browser history")

        # get page source
        pageSource = driver.page_source
        print(pageSource)

        # close driver
        driver.quit()


browserInteraction = BrowserInteraction()
browserInteraction.testMethod()