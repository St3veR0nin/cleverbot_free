from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

class CleverBot:


    def __init__(self):
        """
        Requirements: pyppeteer, asyncio and bs4
        """
        self.element = None
        options = Options()
        options.headless = True 
        self.wd = webdriver.Firefox(options=options)

    def init(self):
        """
        Start the webdriver in headless mode, and install chromium 
        if not available, must be called just one time, until close()
        is called.
        """
        self.wd.get("https://www.cleverbot.com/") 

        self.wd.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/form/input").click()
        time.sleep(0.5)
        self.element =  self.wd.find_element_by_css_selector("#avatarform > input.stimulus")


    def getResponse(self, text):
        """
        Send text to Cleverbot and recieve response
        """
        self.element.send_keys(text)
        self.element.submit()
        time.sleep(4)
        return self.wd.find_element_by_css_selector("#line1 > span.bot").text

    def close(self):
        """
        Close the connection to Cleverbot and closes page and browser
        """
        self.wd.quit()
