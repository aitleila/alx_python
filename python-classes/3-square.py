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
        
        if not isinstance (self, int):
            TypeError("size must be an integer")
        if size < 0:
            ValueError("size must be >= 0")
        self.__size = size

    def area (self):
        """
            current square area
        """
        return self.__size**2
        return area(self.__size**2)

    def perimeter (self):
       4*self.__size

    def set_size (self, new_size):
        self._size = new_size
        if new_size < 0 :
            ValueError ("The size is negative, please enter a new size.")
        
    def self_size(self, value):
        self.__size
        if not isinstance (self, int):
                TypeError("size must be an integer")
        if size < 0:
                ValueError("size must be >= 0")





    



#Instantiation:
   

