#!/usr/bin/python3

"""Unittest filr for max_integer([...])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_list1(self):
        list1 = [1, 2, 3, 4]
        self.assertEqual(max_integer(list1), 4)

    def test_max_list2(self):
        list2 = [5, -10, 2, 0, -2]
        self.assertEqual(max_integer(list2), 5)
