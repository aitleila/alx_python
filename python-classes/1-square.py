#!/usr/bin/python3
"""
        __size (int): The size of the square (private attribute)
"""

class Square:

    """
    This class represents a square with a given size.
    """
    
    def __init__(self, size=0):
        self.__size = size
        if size < 0:
            return ValueError("size must be >= 0")
        if not isinstance (self, int):
            return TypeError("size must be an integer")

    def area (self):
        self.__size**2

    def perimeter (self):
        4*self.__size

    def set_size (self, new_size):
        self._size = new_size
        if new_size <=0 :
            return ValueError ("The size is negative, please enter a new size.")
        
    def get_size (self):
        self.__size


    


