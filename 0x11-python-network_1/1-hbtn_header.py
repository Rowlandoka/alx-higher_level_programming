#!/usr/bin/python3
# Take a url, send a request and display value of header
import urllib.request
import sys


def main():
    """
    Takes a url, send a request and display it values
    """
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))


if __name__ == "__main__":
    main()
