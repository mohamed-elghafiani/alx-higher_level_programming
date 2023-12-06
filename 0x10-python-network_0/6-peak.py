#!/usr/bin/python3
# Technical interview preparation:
""" Finding a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """Return the peak in a list_of_integers"""
    if not list_of_integers:
        return None

    if len(set(list_of_integers)) == 1:
        return list_of_integers[0]

    for i, n in enumerate(list_of_integers[1:-1]):
        if n > list_of_integers[i] and n > list_of_integers[i + 2]:
            return n

    if list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]

    if list_of_integers[-1] > list_of_integers[-2]:
        return list_of_integers[-1]
