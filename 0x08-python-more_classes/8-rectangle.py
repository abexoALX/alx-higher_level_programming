#!/usr/bin/python3
"""This module defines the a Rectangle Object"""


class Rectangle:
    """rectangle class
     Attributes:
             number_of_instances (int): The number of Rectangle instances.
             print_symbol (any): The symbol used for string representation.
    """
    number_of_instances = 0
    print_symbol = "#"
    
    
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
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
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """" Bigger or Equal """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
