#!/usr/bin/python3
""" class my_list"""


class MyList(list):
    """ print sorted list of class"""
    def print_sorted(self):
        print(sorted(self))
