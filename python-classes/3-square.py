#!/usr/bin/python3
"""
        __size (int): The size of the square (private attribute)
"""

class Square:

    """
    This class represents a square with a given size.
    """
    
    def __init__(self, size=0):
        """
        Initialize a Square object with a optional size
        """
        self.__size = size

    @property
    def size(self):
        """
        @property decorater:
        Allows one to create getters and setters method for a private attribute.
        Enables controlled access to that attribute while maintaining encapsulation.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance (value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = value

    def area (self):
        """
        Current square area
        
        """
        return self.__size ** 2
