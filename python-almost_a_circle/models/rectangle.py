#!/usr/bin/python3
"""The file Rectangle inherit from Base"""

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

    @property
    def width(self):
        """
        The getter of the attribute width
        """
        return self.width
    
    @width.setter    
    def width(self, value):
        """
        the setter of the private attribute width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    @property
    def height(self):
        """
        The getter of the attribute height
        """
        return self.height
    
    @height.setter
    def height(self, value):
        """
        The setter of the private attribute height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.height = value

    @property
    def x (self):
        """
        The getter of the attribute x
        """
        return self.x
    
    @x.setter
    def x (self, value):
        """
        The setter of the private attribute x   
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.x = value

    @property
    def y (self):
        """
        The getter of the attribute y
        """
        return self.y
    
    @y.setter
    def y (self, value):
        """
        The setter of the private attribute y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.y = value

    def area(self):
        """
        The area of rectangle
        """
        return self.__width*self.__height
    
    def display(self):
        """Display function with the character #"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print( ' ' *  self.__x  +  '#'  *  self.__width)
    
    def display(self):
        """Display function with the character #"""
        for _ in range(self.__height):
            print('#' * self.__width)

    def __str__(self):
        """
        The Rectangle string
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
    
    def display(self):
        """Display function with the character #"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print( ' ' *  self.__x  +  '#'  *  self.__width)

    def update (self, *args):
        """
        Public method *args
        “no-keyword argument” - Argument order is super important
        """
        num_args = len(args)
        if len(args)>0:
            self.id = args[0]
        if len(args)>1:
            self.width = args[1]
        if len(args)>2:
            self.height = args[2]
        if len(args)>3:
            self.x = args[3]
        if len(args)>4 :
            self.y = args[4]
        
    def update (self, *args, **kwargs):
        """
        Public method *args, **kwargs
        “no-keyword argument” - Argument order is super important
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)      
       
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
        