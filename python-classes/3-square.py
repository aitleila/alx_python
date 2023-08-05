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
        Square object with a optional size

        Args:
            size(int): The size of the Square(default is 0)

        Returns:
            TypeError:If size is not an interger
            ValueError:If size is less than 0
        """
        
        if type(size) is not int (self):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
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
        """
         @size.setter : Decorator used in conjunction with @property to define the setter method for a property
        Returns:
            TypeError:If size is not an interger
            ValueError:If size is less than 0
        """
        if not isinstance (self, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        
        return self.__size == value

    def area (self):
        """
        Current square area
        """
        return self.__size**2
        return area(self.__size**2)

    def perimeter (self):
       """
       Current square perimeter 
       """
       4*self.__size

    def set_size (self, new_size):
        """
        Current square set new size
        """
        self._size = new_size
        if new_size < 0 :
            ValueError ("The size is negative, please enter a new size.")
        
    def get_size (self):
        """
        Current square get size
        """
        self.__size


    



#Instantiation:
   


