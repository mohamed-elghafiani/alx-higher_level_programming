#!/usr/bin/python3

def weight_average(my_list=[]):
    w_average = 0
    weights = 0
    if my_list:
        for (score, weight) in my_list:
            w_average += score * weight
            weights += weight

        w_average = w_average / weights
    return w_average
