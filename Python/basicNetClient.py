#!/usr/local/bin/python3
import socket
import re
from swapFormats import *

def GenerateResponse(serverMessage, sock):
    """ Processes the message from the server and generates a response.

    Parameters:
    serverMessage (byte[]): Message from server in byte[]
    sock (socket): Socket being used for communication

    Returns:
    str: The message to send back to server.
    """

    # Prompt REGEX to match from server. Example equation REGEX in form
    # -5 + 7 - 3 =
    pattern = re.compile("[-]?\d+[+|\-|*|/][-]?\d+([+|\-|*|/][-]?\d+)*=")
    
    # Message from server is a byte[], needs to be converted to Ascii
    asciiSvrMessage = BytesToAscii(serverMessage).replace('\r', '')
    print(asciiSvrMessage)

    # Example check for authentication prompt
    if ("Login please" in asciiSvrMessage):
        return "<loginInfo>\n"
    
    # Example check for the pattern you are looking for
    elif (pattern.match(asciiSvrMessage)):
        # do something here
        return "<yourResponse>\n"

    else:
        # If you don't get the server response you were expecting based
        # on your REGEX. Receive more data and try again. Waits for user
        # input in case you want to break.
        appendedResponse = serverMessage + sock.recv(65536)
        input("Looking for prompt press any key to continue...")
        return GenerateResponse(appendedResponse, sock)


def BasicClient(host, port):
    """ Opens a basic socket to the server host and port, then passes the server message from the
    to GenerateResponse() to process and then send a response.

    Parameters:
    host (str): URL or IP of the server
    port (int): Port to connect to    
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (host, port)
        sock.connect(server_address)
        while (True and not sock._closed):
            serverMessage = sock.recv(65536 * 2)
            response = GenerateResponse(serverMessage, sock)
        
            print("Sending: " + response)
            sock.sendall(response.encode())
    
    except KeyboardInterrupt:
        print("Breaking")

    except Exception as err:
        print("Error " + str(err))

    finally:
        print("Closing Socket")
        sock.close()


host = "127.0.0.1"
port = 1234

BasicClient(host, port)