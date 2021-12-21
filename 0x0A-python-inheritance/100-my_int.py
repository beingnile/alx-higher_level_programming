#!/usr/bin/python3

""" Defines class MyInt inheriting from int inbuilt """


class MyInt(int):
    """ A rebel class with inverted operators """

    def __eq__(self, value):
        """ Invert == operator with != """
        return self.real != value

    def __ne__(self, value):
        """ Invert != operator with == """
        return self.real == value
