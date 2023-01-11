#!/usr/bin/python3
""" appends a text file """


def append_write(filename="", text=""):
    """ appends a text file """
    with open(filename, mode='a', encoding='utf-8') as f:
        return (f.write(text))
