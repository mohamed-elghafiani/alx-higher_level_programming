#!/usr/bin/python3
"""
Rectangle unittest testing
"""
import unittest
from models.rectangle import Rectangle


class RectangleUnitTest(unittest.TestCase):
    """
    Rectangle unittests
    """
    def test_id_is_None(self):
        r = Rectangle(5, 4)
        self.assertEqual(r.id, 1)

    def test_id_is_not_None(self):
        r = Rectangle(5, 4, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_id_is_None_2(self):
        r = Rectangle(5, 4)
        self.assertEqual(r.id, 2)
