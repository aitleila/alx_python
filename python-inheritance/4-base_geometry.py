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
    def area(self):
        if NotImplemented :
            raise " area() is not implemented "
        return super().__area__()
class BaseGeometry(metaclass=BaseGeometryMetaClass):
    """
    A base class representing geometry
    """
    def __dir__(self):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    pass
