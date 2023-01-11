#!/usr/bin/python3
""" writes a text file """


def write_file(filename="", text=""):
    """ writes a text file """
    with open(filename, mode='w', encoding='utf-8') as f:
        return (f.write(text))
