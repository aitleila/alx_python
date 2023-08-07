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

       

        

