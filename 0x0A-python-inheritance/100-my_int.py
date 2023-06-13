#!/usr/bin/python3
"""Defines a rebel class MyInt"""


class MyInt(int):
    """Defines a rebel class MyInt that flips the ==
    and != operators"""
    def __eq__(self, other):
        """Flips operation to !="""
        return not super().__ne__(other)

    def __ne__(self, other):
        """"Flips operation to =="""
        return not self.__eq__(other)
