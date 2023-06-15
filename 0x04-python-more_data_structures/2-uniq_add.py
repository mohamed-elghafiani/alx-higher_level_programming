#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq = set(my_list)
    sum_ = 0
    for i in uniq:
        sum_ += i

    return sum_
