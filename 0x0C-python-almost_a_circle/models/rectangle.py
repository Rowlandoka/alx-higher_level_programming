#!/usr/bin/python3
""" class rectangle"""
from models.base import Base


class Rectangle(Base):
    """ Create the rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialise the class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ get widths"""
        return self.__width

    @property
    def height(self):
        """get the height"""
        return self.__height
    
    @property
    def x(self):
        """Get x"""
        return self.__x
    
    @property
    def y(self):
        """ Get y """
        return self.__y

    @height.setter
    def height(self, value):
        """set the height"""
        self.__height = value

    @width.setter
    def width(self, value):
        """ Set the width"""
        self.__width = value

    @x.setter
    def x(self, value):
        """ Set x """
        self.__x = value

    @y.setter
    def y(self, value):
        """ Set the value of y."""
        self.__y = value


