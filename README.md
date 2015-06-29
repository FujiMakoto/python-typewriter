# python-typewriter
Python Typewriter is a very simple Python module that allows you to print out strings using a "typewriter" like effect. That is, each character is printed out individually with a brief pause in between characters.

![Typewrite Demonstration]
(https://github.com/FujiMakoto/python-typewriter/blob/master/docs/demo.gif)

## Features
By default typewrite always fully prints out a message within 3 seconds. This means that while shorter messages will be outputted at the default pace, the animation for longer messages is dynamically sped up so that the message is still fully printed within a reasonable time frame.

Typewrite also applies brief additional pauses for commas and full stops (., !, ?), providing a more human-like feeling to the animation.

All of these values can be configured at will. The max/min time values as well as the multipliers for commas and stops can be changed or disabled entirely.

## How to use
Using the typewrite function is incredibly simple. Just import the function from the typewriter module and provide a message to print out,
```
from typewriter import typewrite
typewrite('This is a test. Hello world! I am a typewriter, what is your name?')
```
The typewrite function is utilized like so,
```python
typewrite(message, max_time=3, min_time=None, base=0.075, end='\n', **kwargs)
```
##### max_time
Contains the maximum length of time the typewrite animation will take. Change this value to speed up the typewrite animation for long messages. Set to None to disable.

##### min_time
Similarly contains the minimum length of time the typewrite animation will take. Change this value to slow down the typewrite animation for short messages. Set to None to disable.

##### base
Contains the base pause length between characters. Change this value to increase/decrease the default delay between printed out characters.

##### end
Contains the character that is printed out after the animation is completed,

### Keyword arguments
The following keyword arguments can be used to more finely tune the typewrite animation.

##### use_multipliers
When set to False will disable the additional pauses caused by commas and full stops. Defaults to True.

##### comma_multiplier
Contains the base multiplier for commas. Default is 2.0.

##### stop_multiplier
Contains the base multiplier for full stops. Default is 2.5.
