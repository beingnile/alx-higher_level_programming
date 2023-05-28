#!/usr/bin/python3
"""Definrs a Node clas and a SinglyLinkedList class"""


class Node:
    """Defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Gets the node data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the node data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next_node value"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node value"""
        if self.__next_node != None and not isinstance(value, __class__):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Defines a singly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node to the singly linked list"""
        if self.__head == None:
            self.__head = Node(value)
            return
        current = self.__head
        while current.next_node is not None:
            current = current.next_node
        current.next_node = Node(value)

    def __str__(self):
        """Prints each node in stdout"""
        current = self.__head
        while current is not None:
            if current.next_node == None:
                print(current.data, end='')
                break
            print(current.data)
            current = current.next_node

        return ""
