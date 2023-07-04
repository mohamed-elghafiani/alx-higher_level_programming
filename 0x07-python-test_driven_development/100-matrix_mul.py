#!/usr/bin/python3
"""Module to find the multiplication of two matrices
"""


def matrix_mul(m_a, m_b):
    """Calculates the matrix multiplication of two matrices m_a and m_b

    Args:
      m_a: The first matrix (list of lists)
      m_b: The second matrix (list of lists)

    Raises:
      TypeError: If m_a or m_b are not a list of lists of floats/integer
        where every row is of the same size
      ValueError: If m_b or m_b are empty lists or can't be multiplied
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(el, list) for el in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(el, list) for el in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    first_row_size = len(m_a[0])
    for row in m_a:
        isnm = all(isinstance(el, int) or isinstance(el, float) for el in row)
        # is_all_float = all(isinstance(el, float) for el in row)
        if not isnm:
            raise TypeError("m_a should contain only integers or floats")
        if len(row) != first_row_size:
            raise TypeError("each row of m_a must be of the same size")

    first_row_size = len(m_b[0])
    for row in m_b:
        isnm = all(isinstance(el, int) or isinstance(el, float) for el in row)
        # is_all_float = all(isinstance(el, float) for el in row)
        if not isnm:
            raise TypeError("m_b should contain only integers or floats")
        if len(row) != first_row_size:
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_c = []
    for row_a in m_a:
        row_c = []
        # Calculating the transpose of m_b
        m_b_T = [list(col) for col in zip(*m_b)]
        for row_b in m_b_T:
            row_c.append(sum([a * b for (a, b) in zip(row_a, row_b)]))
        m_c.append(row_c)
    return m_c
