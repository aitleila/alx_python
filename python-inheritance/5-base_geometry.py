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
        if value is isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0 :
            raise ValueError("<name> must be greater than 0") 
   