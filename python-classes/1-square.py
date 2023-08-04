#!/usr/bin/python3
"""
        __size (int): The size of the square (private attribute)
"""

class Square:

    """
    This class represents a square with a given size.
    """
    
    def __init__(self, size=0):

        if not isinstance (self, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size


    def area (self):
        return self.__size**2

    def perimeter (self):
        return 4*self.__size

    def set_size (self, new_size):
        self._size = new_size
        if new_size < 0 :
            raise ValueError ("The size is negative, please enter a new size.")
        
    def get_size (self):
        return self.__size


    



