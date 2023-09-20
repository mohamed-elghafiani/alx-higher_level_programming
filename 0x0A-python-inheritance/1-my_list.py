#!/usr/bin/python3
"""MyList Module"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        print(sorted(self))
