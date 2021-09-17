import base64
from enum import Enum

class Formats(str, Enum):
    ASCII = "ascii"
    ASCII_BINARY = "ascii_bin"
    BASE64 = "b64"
    DECIMAL = "dec"
    HEX = "hex"
    OCTAL = "oct"
    

def GetAsciiBytes(inputString):
    return inputString.encode()

def BytesToAscii(inputBytes):
    return inputBytes.decode("ascii")

def GetB64Bytes(inputString):
    return base64.standard_b64decode(inputString)

def BytesToBase64(inputBytes):
    return base64.standard_b64encode(inputBytes).decode(encoding="utf-8")

def GetHexBytesFromAscii(inputString):
    return bytearray.fromhex(inputString)

def BytesToHex(inputBytes):
    return inputBytes.hex()

def GetDecimalBytes(inputInt):
    if (inputInt.bit_length() % 8 != 0):
        numBytes = int((inputInt.bit_length() / 8) + 1)
    else:
        numBytes = int(inputInt.bit_length() / 8)

    return inputInt.to_bytes(numBytes, "big")

def BytesToDecimal(inputBytes):
    return int.from_bytes(inputBytes, "big")

def GetOctalBytes(inputString):
    return GetDecimalBytes(int(inputString, 8))

def BytesToOctal(inputBytes):
    return oct(BytesToDecimal(inputBytes))

def GetAsciiBinBytes(inputString):
    return GetDecimalBytes(int(inputString, 2))

def BytesToAsciiBin(inputBytes):
    return bin(BytesToDecimal(inputBytes))[2::]

def FormatToBytes(originalBase, originalString):
    if (originalBase == "ascii"):
        return GetAsciiBytes(originalString)
    elif (originalBase == "b64"):
        return GetB64Bytes(originalString)
    elif (originalBase == "hex"):
        return GetHexBytesFromAscii(originalString)
    elif (originalBase == "dec"):
        return GetDecimalBytes(int(originalString))
    elif (originalBase == "oct"):
        return GetOctalBytes(originalString)
    elif (originalBase == "ascii_bin"):
        return GetAsciiBinBytes(originalString)

def BytesToFormat(resultBase, originalBytes):
    if (resultBase == "ascii"):
        return BytesToAscii(originalBytes)
    elif (resultBase == "b64"):
        return BytesToBase64(originalBytes)
    elif (resultBase == "hex"):
        return BytesToHex(originalBytes)
    elif (resultBase == "dec"):
        return str(BytesToDecimal(originalBytes))
    elif (resultBase == "oct"):
        return BytesToOctal(originalBytes)[2::]
    elif (resultBase == "ascii_bin"):
        return BytesToAsciiBin(originalBytes)

def ConvertFormats(data, originalBase, newBase):
    dataBytes = FormatToBytes(originalBase, data)
    return BytesToFormat(newBase, dataBytes)

def Test():

    # typesAllow = ["ascii", "b64", "hex", "dec", "oct", "ascii_bin"]

    original = "Th1s is a c0mplicated str1ng wi7h special characters !@#$%^&*()"
    origBytes = FormatToBytes("ascii", original)
    print(original)
    for base in Formats:
    
        result = BytesToFormat(base, origBytes)
        print("Base:" + base)
        print("\tRepresentation: " + result)
        if base != "ascii":
            midFormat = ConvertFormats(original, Formats.ASCII, base)
            result = ConvertFormats(midFormat, base, Formats.ASCII)
            print("\t" + base + " to ASCII: " + result)
        if (result == original):
            print("\t" + base + ": Success")

        else:
            print("\t" + base + "Failure")
