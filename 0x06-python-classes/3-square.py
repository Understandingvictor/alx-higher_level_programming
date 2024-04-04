#!/usr/bin/python3
"""
a moduile that has a class Square
"""


class Square:
    """
    a class sqaure that defines a square
    """
    def __init__(self, size=0):
        """
        Initializes a new square instance.

        Parameters:
            size (int): The size of the square

        Raises TypeError when if size is not integer
        Raises ValueError if size is less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        public instance method which returns the
        current square area
        """
        return self.__size ** 2
