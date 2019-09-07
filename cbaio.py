import asyncio
import pyppeteer as pyp 
from bs4 import BeautifulSoup

class CleverBot:

    browser = None
    page = None
    element = None

    def __init__(self):
        """
        Requirements: pyppeteer, asyncio and bs4
        """
        pass

    async def init(self):
        """
        Start the webdriver in headless mode, and install chromium 
        if not available, must be called just one time, until close()
        is called.
        """
        self.browser = await pyp.launcher.launch()
        self.page = await self.browser.newPage()
        await self.page.goto("https://www.cleverbot.com") 
        self.element =  await self.page.querySelector("input.stimulus")
    

    async def getResponse(self, text):
        """
        Send text to Cleverbot and recieve response
        """
        await self.element.type(text)
        await self.element.press("Enter")
        await asyncio.sleep(3)
        html = await self.page.content()
        soup = BeautifulSoup(html, features="html.parser")
        return soup.find("p", {"id":"line1"}).getText()

    async def close(self):
        """
        Close the connection to Cleverbot and closes page and browser
        """
        await self.page.close()
        await self.browser.close()
