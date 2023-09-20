#!/usr/bin/python3
"""MyList Module"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
        return sorted_list
