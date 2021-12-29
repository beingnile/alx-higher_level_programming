#!/usr/bin/python3
"""
Class Square that defines a square.
"""


class Square:
    """
    Class defining a square object.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size (int): The size of the square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Get Square size.
        Returns:
            The square size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
         Raises:
            TypeError: If size is not an integer.
            ValueError: If size is < 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns:
            Area of the defined square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the # character."""
        for row in range(0, self.__size):
            [print("#", end="") for col in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
