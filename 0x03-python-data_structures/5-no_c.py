#!/usr/bin/python3

def no_c(my_string):
    no_c_str = ""
    for el in my_string:
        if el not in "cC":
            no_c_str += el
    return no_c_str
