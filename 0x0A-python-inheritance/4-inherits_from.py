#!/usr/bin/python3
""" 
 Check if object is direct or indirect instance of a subclass
"""

def inherits_from(obj, a_class):
    """ Return the instance of subclass"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
