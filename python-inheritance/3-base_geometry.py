#!/usr/bin/python3
"""  
    A base class representing geometry.
    
"""
class BaseGeometry:
    """
    This is empty class
    """

class BaseGeometryMetaClass():
    """
    Removing __init_subclass
    """
    def __dir__(cls) -> None:
        attributes = super().__dict__()
        n_attributes = []
        for attr in attributes:
            if attr !=' __init_subclass__':
                n_attributes.append(attr)
        return n_attributes


class BaseGeometry(MetaClass=BaseGeometryMetaClass):
    """
    __init_subclass
    """
    def __dir__(cls):
        return [attribute for attribute in super.__dict__() if attribute !='__init_subclass__']

