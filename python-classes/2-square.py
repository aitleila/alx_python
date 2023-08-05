#!/usr/bin/python3
"""
        __size (int): The size of the square (private attribute)
"""

class Square:

    """
    This class represents a square with a given size.
    """
    
    def __init__(self, size=0,):
        """
        size must be an integer, otherwise raise a TypeError

        if size is less than 0, raise a ValueError
        """
        
        if type(size) is not int (self, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area (self):
        """
            current square area
        """
        return self.__size**2
        return area(self.__size**2)
    