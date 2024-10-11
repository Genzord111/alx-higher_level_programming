#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class initiates testing of max_integer function"""

    def test_max_integer(self):
        """Test 1"""
        self.assertEqual(max_integer([1, 7, 4, 1.5]), 7)
        self.assertEqual(max_integer([10.5, 6.78, 5]), 10.5)
        self.assertEqual(max_integer([-3, -5, -9]), -3)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([[1, 2], [3, 4], [5, 6]]), [5, 6])
        self.assertEqual(max_integer([[1], [2], [3]]), [3])
        self.assertEqual(max_integer("Hello"), 'o')
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')
