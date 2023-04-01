#!/usr/bin/python3
"""
Python scripts that takes a url, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from sys import argv
req = Request(argv[1])

if __name__ == "__main__":
    try:
        response = urlopen(req)
    except URLError as e:
        if hasattr(e, 'reason'):
            print("We failed to reach the server. ")
            print("Reason: ", e.reason)
        elif hasattr(e, 'code'):
            print("The server couldn\t fulfil the request")
            print("Error code: ", e.code)
    else:
        print(response.decode())
