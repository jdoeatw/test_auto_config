from selenium import webdriver
import os


class RunChromeTests():
    # http://chromedriver.storage.googleapis.com/index.html

    def test(self):

        driverLocation = "/Users/george/Documents/workspace/selenium/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(driverLocation)
        # Open the provided URL
        driver.get("http://www.letskodeit.com")


ch = RunChromeTests()
ch.test()