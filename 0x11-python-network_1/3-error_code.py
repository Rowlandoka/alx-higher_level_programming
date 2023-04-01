#!/usr/bin/python3
"""
Python scripts that takes a url, sends a request to the URL and displays the body of the response (decoded in utf-8).
"""
from urllib.request import urlopen
from sys import argv
from urllib.error import HTTPError

if __name__ == '__main__':
    try:
        with urlopen(argv[1]) as response:
            res = response.read()
    except HTTPError as e:
        print("Error code:", e.code)
    else:
        print(res.decode())
