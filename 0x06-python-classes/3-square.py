#!/usr/bin/python3
"""
This module defines a Square class and initialise its size
Its implements value and type checks for its attributes
"""


class Square:
    """Square implementation"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        area = self.__size * self.__size
        return area
