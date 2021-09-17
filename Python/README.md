# Python CTF Helper Scripts

## Description
List of Python scripts with helpers to address random of CTF tasks encountered.

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