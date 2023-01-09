#!/usr/bin/python3

def lookup(obj):
    """Return a list of attributes and methods of an object."""
    return([x for x in dir(obj)])
