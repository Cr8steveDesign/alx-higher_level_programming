#!/usr/bin/python3

"""A Square class"""


class Square:
    """An ampty class Square that defines a square.
    It currently has no attributes nor properties.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialization method of the class
                Args:
                        size (int): Size of the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Size property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the private instance attribute __size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Position property getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for the position attribute"""
        if not isinstance(value, tuple) or len(value) != 2\
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculate the area of the square instance
                Returns:
                        Integer: Square of the size
                """
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with character #
             Returns:
                Really nothing sha
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
