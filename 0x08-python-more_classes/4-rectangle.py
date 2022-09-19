#!/usr/bin/python3
"""This module defines the a Rectangle Object"""


class Rectangle:
    """rectangle class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """ getter """
        return self.__width
    
    @width.setter
    def width(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
    
    @property
    def height(self):
        """ getter """
        return self.__height
    
    @height.setter
    def height(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
    
    def area(self):
        """ area calculate """
        return self.__width * self.__height
    
    def perimeter(self):
        """ permeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
     
    def __str__(self):
        """ This method returns the string representation of the object """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            r = "\n".join(["#" * self.__width for i in range(self.__height)])
            return r
     
     def __repr__(self):
         """ object string format """
         return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
