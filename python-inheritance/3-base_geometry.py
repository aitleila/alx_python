#!/usr/bin/python3
"""  A base class representing geometry.
    This class is intended to be used as a base for other geometry-related classes.
    It currently does not have any attributes or methods defined."""
class BaseGeometry:
    """This is empty class"""

class BaseGeometryMetaClass(type):
    """__init_subclass"""
    def __dir__(cls):
        return [attribute for attribute in super.__dict__() if attribute !='__init_subclass__']

class BaseGeometry(MetaClass=BaseGeometryMetaClass):
    """Removing __init_subclass"""
    def __dir__(cls):
        return [attribute for attribute in super.__dict__() if attribute !='__init_subclass__']
    pass
