#!usr/bin/python3
"""Base class unittests"""
import unittest
from models.base import Base


class BaseClassUnittest (unittest.TestCase):
    def test_id_is_None(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_is_None_2(self):
        b = Base()
        self.assertEqual(b.id, 2)

    def test_id_is_not_None(self):
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_id_is_None_3(self):
        b = Base()
        self.assertEqual(b.id, 3)
