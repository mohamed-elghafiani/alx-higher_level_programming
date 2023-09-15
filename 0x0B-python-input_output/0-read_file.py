#!/usr/bin/python3

"""Reading and printing the contents of a file
"""


def read_file(filename=""):
    """reads and prints the contents of a file
    """
    with open(filename, encoding="utf-8") as f:
        content = f.read()
        if len(content) > 1:
            print(content[:-1])
