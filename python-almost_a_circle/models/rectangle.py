#!/usr/bin/python3
"""
The file Rectangle inherist from Base
"""
from models.base import Base
        
class Rectangle(Base):
    """
    The Class Rectangle inherits from parent Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """The Class Constructor"""        
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def get_width(self):
        """
        The getter of the attribute width
        """
        return self.__width
        
    def set_width(self, value):
        """
        the setter of the private attribute width
        """
        if not isinstance(self, value):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    def get_height(self):
        """
        The getter of the attribute height
        """
        return self.__height
    
    def set_height(self, value):
        """
        The setter of the private attribute height
        """
        if not isinstance(self, value):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    def get_x (self):
        """
        The getter of the attribute x
        """
        return self.__x
    
    def set_x (self, value):
        """
        The setter of the private attribute x   
        """
        if not isinstance(self, value):
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    def get_y (self):
        """
        The getter of the attribute y
        """
        return self.__y
    
    def set_y (self, value):
        """
        The setter of the private attribute y
        """
        if not isinstance(self, value):
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value

    
    
        

