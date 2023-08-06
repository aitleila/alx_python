#!/usr/bin/python3
"""
    A base class representing geometry.

    """
class BaseGeometry:
    """
    A base class representing geometry.
    """
        
class BaseGeometryMetaClass(type):
    """
    A base class representing geometry
    """

    def __dir__(cls):
        return[attribute for attribute in super().__dir__() if attribute != '__init_subclass__'] 
    
class BaseGeometry(metaclass=BaseGeometryMetaClass):
    """
    A base class representing geometry
    """
    def __dir__(self):
        """
        The attributes
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
    def area(self):
        """
         Calculate the area of the geometry
         Raises:
         Exception : This method is not implemented in the base class
        """
        raise Exception('area() is not implemented')
    
    def integer_validator(self, name, value):
        """
        Validate an integer value
        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less than or equal to 0
        """
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
        Returns:
            The area of the rectangle (width * height)
        """
        area = self.__width * self.__height
        return area
    
    def __str__(self):
        """
        Return a string representation of the rectangle
        Returns:
         str: A string with the rectangle description.
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
        return f"[Square] {self.__size}"
    