#!/usr/bin/python3

""" Module class BaseGeometry"""


class BaseGeometry:
    """ Defines a class """
    def area(self):
        """
        Raises:
            Exception with message "area() is not implemented"
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Validates a value
        Args:
            name (str): The Object name
            value (int): An integer
        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less tha or equal to 0
        """
        self.name = name
        if type(value) != int:
            raise TypeError(self.name + ' must be an integer')
        elif value <= 0:
            raise ValueError(self.name + ' must be greater than 0')
        self.value = value
