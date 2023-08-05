#!/usr/bin/python3
"""This is empty class"""
class BaseGeometry:
    """This is empty class"""

class BaseGeometryMetaClass(type):
    """Removing __init_subclass"""
    def __dir__(cls):
        return [attribute for attribute in super.__dict__() if attribute !='__init_subclass__']

class BaseGeometry(MetaClass=BaseGeometryMetaClass):
    """Removing __init_subclass"""
    def __dir__(cls):
        return [attribute for attribute in super.__dict__() if attribute !='__init_subclass__']