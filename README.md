# cleverbot-aio-free
Free version of the Cleverbot API, that supports asyncio

To use this library, you will need the latest version of **pypeteer**, which you can find at this link https://github.com/miyakogi/pyppeteer

**asyncio** and **bs4** are required too.


Once you have all the required packages, you're ready to use this simple library!

## Example of making a request and getting the response string:

```python

from cleverbot-aio-free import CleverBot

#Instantiate the class
cb = CleverBot()

#The first time you call init(), pypeteer will download the chromium browser, 
#that is necessary to use this library.
#This is done only one time, i suggest you call this function in a test script,
#before using it in your programs
#Subsequent calls to init () will not download anything.
cb.init()

#After initialization you can send text to Cleverbot and recieve the text response in just one line...
text = "Hello"

response = cb.getResponse(text)

#When you want to reset the chat, you can close the browser session with...
cb.close()

```

That's it! I hope this library will help lots of people build their chatbots.
