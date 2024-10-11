#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
"""This is a unittest module """


class TestMaxInteger(unittest.TestCase):
    """Class initiates testing of max_integer function"""

    def test_max_integer(self):
        """Test 1"""
        self.assertEqual(max_integer([1, 7, 4, 1.5]), 7)
        self.assertEqual(max_integer([10.5, 6.78, 5]), 10.5)
        self.assertEqual(max_integer([-3, -5, -9], -3)
        self.assertEqual(max_integer([], None)
