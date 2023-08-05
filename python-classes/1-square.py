#!/usr/bin/python3
"""
        __size (int): The size of the square (private attribute)
"""

class Square:

    """ This class represent square of sizes """
    
    def __init__(self, size=0,):

        """size must be an integer, otherwise raise a TypeError"""

        if not isinstance(self, int):
            raise TypeError("size must be an integer")
        if size < 0 :
            raise ValueError("size must be >= 0")
        
        self.__size = size
