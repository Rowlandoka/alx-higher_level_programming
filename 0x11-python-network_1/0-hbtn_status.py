#!/usr/bin/python3
# fetches a website
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        content = resp.read()
        url = content.decode('utf-8')
        typed = resp.info()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(url))
