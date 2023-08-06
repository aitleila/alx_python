#!/usr/bin/python3
"""
    A base class representing geometry.

    """
class BaseGeometry:
    """
    A base class representing geometry.
    """
        
class BaseGeometryMetaClass(type):

    def __dir__(cls):
        return[attribute for attribute in super().__dir__() if attribute != '__init_subclass__'] 
    
class BaseGeometry(metaclass=BaseGeometryMetaClass):
    """
    A base class representing geometry
    """
    def __dir__(self):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
    def area(self):
        raise Exception('area() is not implemented')
    
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 :
            raise ValueError("{} must be greater than 0".format(name))
        
class Rectangle(BaseGeometry):
    """ 
    This is a class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        width and height must be positive integers, validated by integer_validator
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
    
    def area (self):
        """ 
        Calculate the area of the rectangle
        """
        area = self.__width * self.__height
        return area
    
    def __str__(self):
        """
        Return a string representation of the rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
    
class Square(Rectangle):
    """ 
    This is a class Square that inherits from class Rectangle
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
        """
        return self.__size**2
    
    def __str__(self):
        """
        Return a string representation of the square
        """
        return f"[Square] {self.__size}"
    