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

    def to_dictionary(self):
        """dictionary"""
        dic = {'id': self.id, 'width': self.width, 'height': self.height,
               'x': self.x, 'y': self.y}
        return dic

    def update(self, *args, **kwargs):
        """updates attributes"""
        if args:
            i = 0
            keys = ['id', 'width', 'height', 'x', 'y']
            for arg in args:
                setattr(self, keys[i], arg)
                i += 1
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def validator(self, name, value):
        """validates the shit out of it"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if (name is 'width' or name is 'height') and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if (name is 'x' or name is 'y') and value < 0:
            raise ValueError("{} must be >= 0".format(name))

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
        self.validator("height", value)
        self.__height = value

    @width.setter
    def width(self, value):
        """ Set the width"""
        self.validator("width", value)
        self.__width = value

    @x.setter
    def x(self, value):
        """ Set x """
        self.validator("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """ Set the value of y."""
        self.validator("y", value)
        self.__y = value

    def area(self):
        """Gets the area of rectangle"""
        return self.height * self.width

    def display(self):
        """ Prints a rectangle of hashes"""
        print('\n' * self.y, end="")
        print(''.join(' ' * self.x + '#' * self.width + '\n'
                      for times in range(self.height)), end="")

    def __str__(self):
        """gets rectangle"""
        return "[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__, self.id, self.x, self.y,
            self.width, self.height)
