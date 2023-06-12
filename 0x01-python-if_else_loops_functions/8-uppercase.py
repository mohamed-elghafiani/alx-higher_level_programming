#!/usr/bin/python3

def uppercase(str_):
    ustr = ""
    for c in str_:
        if ord(c) in range(97, 123):
            uc = chr(ord(c) - (ord('a') - ord('A')))

        else:
            uc = c
        ustr += uc
    print(ustr)
