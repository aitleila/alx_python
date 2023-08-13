#!/usr/bin/python3

"""This is a Full Rectangle that inherit from BaseGeometry"""

Rectangle = __import__('7-rectangle').Rectangle

"""The file Rectangle from 7-rectangle"""
    
class Square(Rectangle):

    """ 
    This is a class Square that inherits from class Rectangle
    __init__(self, size): Initialize a square with size
    """

    def __init__(self, size):

        """ 
        Initialize a square with size
        """

        self.__size = size
        self.integer_validator("size", size)
    
    def area(self):

        """
        Calculate the area of the square
        Returns:
            The area of the square (size **2)
        """

        return self.__size**2
    
    def __str__(self):

        """
        Return a string representation of the square
        Returns:
         str: A string with the square description.
        """

        return f"[Retangle] {self.__size}/{self.__size}"
    