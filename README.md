# cleverbot_free
Free version of the Cleverbot API.

To Download: ```pip install cleverbot-free --upgrade```


## Example of making a request and getting the response string:

```python

from cleverbot_free.cbaio import CleverBot

#Instantiate the class
cb = CleverBot()

def main():
"""
The first time you call init(), selenium will download the chromium browser, 
that is necessary to use this library.
This is done only one time, i suggest you call this function in a test script,
before using it in your programs
Subsequent calls to init () will not download anything.
"""
    cb.init()
"""
After initialization you can send text to Cleverbot and recieve the text response in just one line...
"""
    response = cb.getResponse("Hello")
    print(response)
#When you want to reset the chat, you can close the browser session with...
    cb.close()

#If you're using python >= 3.7
main()
```

## Simple example of a continous chat

```python
from cleverbot_free.cbaio import CleverBot

cb = CleverBot()

def main():
    cb.init()
    while(True):
        text = input("Say something to CleverBot:")
        if text.lower().find("end") != -1:
            break
        response = cb.getResponse(text)
        print(response)
    cb.close()

main()
```

That's it! I hope this library will help lots of people build their chatbots.
