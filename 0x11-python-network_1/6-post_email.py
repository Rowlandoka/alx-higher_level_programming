#!/usr/bin/python3
"""
Takes in a url and an email
"""
import requests
import sys

if __name__ == "__main__":
    payload = {'email': sys.argv[2]}
    res = requests.post(sys.argv[1], data=payload)
    print(res.text)
