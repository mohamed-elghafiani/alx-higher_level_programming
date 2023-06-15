#!/usr/bin/python3

def common_elements(set_1, set_2):
    c_set = set()
    for a in set_1:
        if a in set_2:
            c_set.add(a)
    return c_set
