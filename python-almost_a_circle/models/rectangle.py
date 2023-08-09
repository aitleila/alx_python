#!/usr/bin/python3
"""
This is a class rectangle that defines a square

"""
class Base:
    """
    This class represent the base class

    """
    __nb_objects = 0

    def __init__(self, id=None): 
        """
        The id here is a private instance attribute

        """
      
        if id is not None:
            self.id=id
        else:
            Base.__nb_objects +=1 
            self.id = Base.__nb_objects
        
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
        return self.__width
    
    @width.setter    
    def width(self, value):
        """
        the setter of the private attribute width
        """
        if not isinstance(self, value):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        The getter of the attribute height
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        The setter of the private attribute height
        """
        if not isinstance(self, value):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x (self):
        """
        The getter of the attribute x
        """
        return self.__x
    
    @x.setter
    def x (self, value):
        """
        The setter of the private attribute x   
        """
        if not isinstance(self, value):
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y (self):
        """
        The getter of the attribute y
        """
        return self.__y
    
    @y.setter
    def y (self, value):
        """
        The setter of the private attribute y
        """
        if not isinstance(self, value):
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """
        The area of rectangle
        """
        return self.__width*self.__height
    
    def display(self):
        """Display function"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print( ' ' *  self.__x  +  '#'  *  self.__width)
    
    def display(self):
        """Display function"""
        for _ in range(self.__height):
            print('#' * self.__width)

    def __str__(self):
        """
        The Rectangle string
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
    
    def display(self):
        """Display function"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print( ' ' *  self.__x  +  '#'  *  self.__width)

    def update (self, *args):
        """
        Public method *args
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
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, args in enumerate(args):
                setattr(self,attributes[i], args)
        if len(kwargs) == 2:
            result = 1
        else:
            for key, value in kwargs.items():
                setattr(key, value, args)
        