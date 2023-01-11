#!/usr/bin/python3
""" Reads a file """


def read_file(filename=""):
    """ Read a file """
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
