#!/usr/bin/python3
# fetches a website
import urllib.request


def main():
    """
    fetches url using urllib package
    """
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        content = resp.read()
        url = content.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(url))


if __name__ == "__main__":
    main()
