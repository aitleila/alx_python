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
        
        Args:
            size(int): The size of the Square(default is 0)
        Raises:
            TypeError:If size is not an interger
            ValueError:If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")      
        self.__size = size

    def area (self):
        """
            current square area
        """
        return self.__size**2
    