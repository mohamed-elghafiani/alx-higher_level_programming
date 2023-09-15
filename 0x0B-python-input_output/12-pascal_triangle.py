#!/usr/bin/python3
"""Pascal triangle module"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
       the Pascal's triangle of n
    """
    if n <= 0:
        return []

    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    else:
        list_ = [[1], [1, 1]]

        nn = 2
        while nn < n:
            i = 1
            line = [1]
            while i < len(list_[nn - 1]):
                line.append(list_[nn - 1][i - 1] + list_[nn - 1][i])
                i += 1
            line.append(1)
            list_.append(line)
            nn += 1

        return list_
