#!/usr/bin/python3

"""Appending to a file
"""


def append_write(filename="", text=""):
    """Appends text to file
    """
    with open(filename, "a", encoding="utf-8") as f:
        count = f.write(text)

    return count
