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

    @property

    def size(self):
        """
        @property decorater:
        Allows one to create getters and setters method for a private attribute.
        Enables controlled access to that attribute while maintaining encapsulation.
        """
        self.__size

    @size.setter

    def size(self, value):
        """
         @size.setter : Decorator used in conjunction with @property to define the setter method for a property
        Returns:
            TypeError:If size is not an interger
            ValueError:If size is less than 0
        """
        if not isinstance (value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = value

    def area (self):
        """
        Current square area
        Returns:
            int: The area of the square.
        """
        return area(self.__size ** 2)
