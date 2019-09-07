# cleverbot_aio_free
Free version of the Cleverbot API, that supports asyncio

To use this library, you will need the latest version of **pypeteer**, which you can find at this link https://github.com/miyakogi/pyppeteer

**asyncio** and **bs4** are required too.


Once you have all the required packages, you're ready to use this simple library!

## Example of making a request and getting the response string:

```python

from cleverbot_aio_free.cbaio import CleverBot

#Instantiate the class
cb = CleverBot()

async def main():
"""
The first time you call init(), pypeteer will download the chromium browser, 
that is necessary to use this library.
This is done only one time, i suggest you call this function in a test script,
before using it in your programs
Subsequent calls to init () will not download anything.
"""
    await cb.init()

#After initialization you can send text to Cleverbot and recieve the text response in just one line...

    response = await cb.getResponse("Hello")
    print(response)
#When you want to reset the chat, you can close the browser session with...
    await cb.close()

#If you're using python >= 3.7
asyncio.run(main)
"""
with python <= 3.6 < 3.7
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
"""
```

## Simple example of a continous chat

```python
from cleverbot_aio_free.cbaio import CleverBot

cb = CleverBot()

async def main():
    await cb.init()
    while(True):
        text = input("Say something to CleverBot:")
        if text.lower().find("end") != -1:
            break
        response = await cb.getResponse(text)
        print(response)
    await cb.close()

asyncio.run(main())
"""or
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
"""
```

That's it! I hope this library will help lots of people build their chatbots.
