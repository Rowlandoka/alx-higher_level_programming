#!/usr/bin/python3
# Take a url, send a request and display value of header
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
