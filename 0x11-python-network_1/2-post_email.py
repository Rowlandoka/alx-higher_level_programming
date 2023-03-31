#!/usr/bin/python3
# takes a url and email and make post request
import urllib.request
import urllib.parse
import sys


def main():
    """
    Post an email into a url as parameter and display the body
    """
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')
    resp = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(resp) as response:
        thisPage = response.read().decode('utf-8')
        print(thisPage)


if __name__ == "__main__":
    main()
