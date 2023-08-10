#!/usr/bin/python3
"""The file Square inherit from Rectangle"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    The Class Square inherits from Rectangle

    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
            """
            The Square string
            """
            return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.height)
    @property
    def size(self):
        """The getter and setter attributes height"""
        return self.height

    @size.setter
    def size(self, value):
        """The private instance attributes height with setter method"""
        self.width = value
        self.height = value
    