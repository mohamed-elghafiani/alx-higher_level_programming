#!/usr/bin/python3

def itemgetter(item):
    return item[0]


def print_sorted_dictionary(a_dictionary):
    sorted_by_keys = sorted(a_dictionary.items(), key=itemgetter)
    for key, val in sorted_by_keys:
        print(f"{key}: {val}")
