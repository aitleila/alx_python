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
        if type is not int(self, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else: 
            self.__size == size

    def area (self):
        self.__size**2

    def perimeter (self):
       4*self.__size

    def set_size (self, new_size):
        self._size == new_size
        if new_size < 0 :
            raise ValueError ("The size is negative, please enter a new size.")
        
    def get_size (self):
        self.__size


    



#Instantiation:
   


