#!/usr/bin/python3
""" class MyList"""


class MyList(list):
    """A subclass of a list"""
    def __init__(self):
        """Initialise the instance"""
        super().__init__()

    def print_sorted(self):
        """ print sorted list of class"""
        print(sorted(self))
