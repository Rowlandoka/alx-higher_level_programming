#!/usr/bin/python3
# takes a url and email and make post request
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        thisPage = response.read().decode('utf-8')
        print(thisPage)
