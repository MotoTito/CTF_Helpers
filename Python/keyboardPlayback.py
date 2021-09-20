import sys
import keyboard
import time

"""
Author: Humberto "Tito" Nieves
Date: 21JUL2020

Requirements: pypi module `keyboard`

Summary: This script uses the virtual keyboard provided by the PyPi module keyboard. It needs to be installed using pip.
The script will take the string in the variable stringToReplay and retype whereever you are currently focused. There is 
a delay of 3 seconds from when the method is called to when it starts to type on the Virtual Keyboard. This can 
be into a VM, into a web page, etc. Be careful because if you click on say the desktop or some other screen that doesn't 
take keyboard input, the script will continue to type on the virtual keyboard passing said input to whatever program is 
currently open and in the foreground. For example, if the URL bar is not focused the string of characters will be passed 
as keypresses to the open browser.

You need to wait for it to complete. It can only accept ASCII characters. Characters outside of this range will throw
an error. It does not use the functionality for special keys such as ctrl, tab, etc.

"""

def ReplayString(stringToReplay: str, waitSeconds:int=3):

  shiftChars='''~!@#$%^&*()_+{}|:"<>?'''
  print(waitSeconds)
  time.sleep(waitSeconds)

  for char in stringToReplay:
    if char.isupper():
      keyboard.press('shift')
      keyboard.press_and_release('shift+' + char)
    elif char == '+':
      keyboard.press('shift')
      keyboard.press_and_release('plus')
    elif char in shiftChars:
      keyboard.press('shift')
      keyboard.press_and_release('shift+' +char)
    else:
      keyboard.press_and_release(char)
