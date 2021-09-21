# Python CTF Helper Scripts

## Description
List of Python scripts with helpers to address random CTF tasks encountered.

### swapFormats
Takes a string in one format and swaps it into another format, for example takes an ASCII string "ABCD" and changes it to a string in its HEX representation "41424344". There is a `Formats` class with:
- ASCII
- BASE64
- Binary represented in ASCII
- Hexadecimal
- Octal

```
original = "ABCD"
hexRep = ConvertFormats(input, Formats.ASCII, Formats.HEX)
# hexRep -> "41424344"

binaryRep = ConvertFormats(input, Formats.ASCII, Formats.ASCII_BINARY)
# binaryRep -> "1000001010000100100001101000100"

asciiRep = ConvertFormats(binaryRep, Formats.ASCII_BINARY, Formats.ASCII)
# asciiRep -> "ABCD"
```

### keyboardPlayback
Takes a string variable and replays it keystroke by keystroke. Written if there is a VM or window that you cannot copy into. Allows you to write your string/code and then click on the input and have simulated keyboard inputs copy the string over for you. From when you click run it will wait 3 seconds before it starts typing. This can be set with the `waitseconds` parameter. It isn't very quick, but is functional. Requires [keyboard](https://pypi.org/project/keyboard/) to be imported from pypi.

```
test = """
This is my multiline string
With lines
"""

timeToWait = 5

#Will wait 5 seconds before it starts typing the string.
ReplayString(test, timeToWait)

```

### basicNetClient
A basic network client that connects to a server and processes the response and replies. For example, a CTF puzzle where the server would send an equation such as `-72*3+900/345=?` and the response had to be within seconds. The server message would be passed to `GenerateResponse` where it would be parsed and a reply sent back to the server, and it would loop until an unexpected response would appear.
