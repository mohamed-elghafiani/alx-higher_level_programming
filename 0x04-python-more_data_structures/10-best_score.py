#!/usr/bin/python3

def getscore(item):
    return item[1]


def best_score(a_dictionary):
    if a_dictionary:
        sorted_dict = sorted(a_dictionary.items(), key=getscore, reverse=True)
        best_score = sorted_dict[0][0]
        return best_score
    else:
        return None
