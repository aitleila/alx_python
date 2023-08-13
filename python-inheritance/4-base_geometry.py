#!/usr/bin/python3
"""
    A base class representing geometry.

    """
class BaseGeometry:
    """
    A class representing geometry.
    """
    def __dir__(cls) -> None:
        """Remove __init_subclass"""
        attributes = super().__dir__()
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
class BaseGeometryMetaClass(type):

    def __dir__(cls)->None:
        """
        Remove __init__ subclass
        """
        attributes = super().__dir__()
        return[attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    
class BaseGeometry(metaclass=BaseGeometryMetaClass):
    """
    A base class representing geometry
    """
    def area(self):
        """Raise an exception that area is not implemented"""
        raise Exception("area() is not implemented")
    
    def __dir__(cls) -> None:
                """Removing __init_subclass"""
                attributes = super().__dir__()
                return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
