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
    """ This is a class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """width and height must be positive integers, validated by integer_validator"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
    
    def area (self):
        area = self.__width * self.__height
        return area
    
    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
    
        
