#!/usr/bin/python3

def remove_char_at(str_, n):
    if n <= len(str_) and n >= 0:
        if n == len(str_):
            return str_[:n]
        else:
            return str_[:n] + str_[n+1:]
    else:
        return str_
