#!/usr/bin/python3

"""Define a class Rectangle."""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width=0, height=0):
        """ Initialise a new Rectangle. 
        Args: 
            width(int): the width of rectangle.
            height(int): the height of rectangle.
        """

        self.__width = width
        self.__height = height
