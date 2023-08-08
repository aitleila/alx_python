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
    This class represent rectangle of sizes
    """

    __width = Base.width
    """
    Private instance attributes
    """
    def get_width(self):
        """
        The getter of the attribute width
        return value width
        """
        return self.width
        
    def set_width(self, value):
        """
        the setter of the attribute width
        """
        self.width = value

    __height = Base.height
    """
    Private instance attributes
    """

    def get_height(self):
        """
        The getter of the attribute height
        return value height
        """
        return self.height
    
    def set_height(self, value):
        """
        The setter of the attribute height
        """
        self.height = value
    
    __x = Base.x
    """
    Private instance attributes
    """
    
    def get_x (self):
        """
        The getter of the attribute x
        return self x 
        """
        return self.x
    
    def set_x (self, value):
        """
        The setter of the attribute x   
        """
        self.x = value

    __y = Base.y
    """
    Private instance attributes
    """
    
    def get_y (self):
        """
        The getter of the attribute y
        return : self y
        """
        return self.y
    
    def set_y (self, value):
        """
        The setter of the attribute y
        """
        self.y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor
        Call the super class with with use the logic of the __init__ of the Base class
        """
        super(Base).__init__(width)
        """
        Call the super class
        """
        self.width = width
        super(Base).__init__(height)
        """
        Call the super class
        """
        self.height = height
        super(Base).__init__(x)
        """
        Call the super class
        """
        self.x=x
        super(Base).__init__(y)
        """
        Call the super class
        """
        self.y = y
        super(Base).__init__(id)
        """
        Call the super class
        """
        self.id = id
    
        

