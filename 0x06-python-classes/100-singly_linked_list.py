#!/usr/bin/python3

"""
    This module defines the Node class and the SinglyLinkedList class
"""


class Node():
    """
        This class represents the Node
    """
    def __init__(self, data, next_node=None):
        """
            An instantiator for the node instancee
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
            Gets the data of the node

            Returns:
                (int) : The node's data
        """
        return self.__data

    @data.setter
    def data(self, data):
        """
            Sets the data of the node
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = data

    @property
    def nex_node(self):
        """
            Gets the next node in the linked list
        """
        return self.__next_node

    @nex_node.setter
    def next_node(self, next_node):
        """
            Sets the next node in a linked list
        """
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node


class SinglyLinkedList():
    """
        This class represents the singly linked list
    """
    __sll = []

    def __init__(self):
        """
            Instantiator of the singly linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        """
            Inserts a new Node into the correct sorted position in the list
                (increasing order)
            Args:
                value (int): The value of the node
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value <= self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            node = self.__head
            while node.next_node is not None:
                if value <= node.next_node.data:
                    break
                node = node.next_node
            new_node.next_node = node.next_node
            node.next_node = new_node

    def __str__(self):
        if self.__head is None:
            return ""

        node = self.__head
        data = []
        while node:
            data.append(str(node.data))
            node = node.next_node
        return "\n".join(data)
