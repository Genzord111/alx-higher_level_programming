"""This module contain unittest for the rectangle class"""
from models.rectangle import Rectangle
from models.square import Square
import unittest

class TestRectangle(unittest.TestCase):
    """Test class"""
    def test_init_(self):
        """Tests class instantiation"""
        r1 = Rectangle(5, 3)
        r2 = Rectangle(10, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(print(r1.id), f"1")
        self.assertEqual(print(r2.id), f"2")
        self.assertEqual(print(r3.id), f"1")


if __name__=='__main__':
    unittest.main()
