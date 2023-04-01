#!/usr/bin/python3
# fetches a website
from urllib.request import urlopen


def main():
    """
    fetches url using urllib package
    """
    with urlopen('https://alx-intranet.hbtn.io/status') as resp:
        content = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))


if __name__ == "__main__":
    main()
