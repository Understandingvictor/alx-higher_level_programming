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
        self.__size = size

    @property
    def size(self):
        """ The function implementation"""
        return self.__size

    @size.setter
    def size(self, value):
        """The function implementation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        public instance method which returns the
        current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        public instance method which prints in stdout
        the square with the character #
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
