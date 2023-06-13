#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is not None and tuple_b is not None:
        tuple_2 = ()
        for i in range(2):
            if i < len(tuple_a):
                a = 0 if not tuple_a[i] else tuple_a[i]
            else:
                a = 0
            if i < len(tuple_b):
                b = 0 if not tuple_b[i] else tuple_b[i]
            else:
                b = 0
            tuple_2 += (a+b, )
    return tuple_2
