#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared = []
    for el in matrix:
        sq = list(map(lambda x: x**2, el))
        squared.append(sq)
    return squared
