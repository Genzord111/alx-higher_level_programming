"""This module contain unittest for the rectangle class"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestRectangle(unittest.TestCase):
    """Test class"""

    def setUp(self):
        """Sets up instances for testing"""
        Base._Base__nb_objects = 0
        self.r1 = Rectangle(5, 3)
        self.r2 = Rectangle(10, 2)
        self.r3 = Rectangle(10, 2, 0, 0, 12)

    def test_init_(self):
        """Tests initialization of class"""

        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 12)

        self.assertIsInstance(self.r1, Rectangle)
        self.assertIsInstance(self.r2, Base)

        self.assertFalse(self.r1 == self.r2)
        self.assertIsNot(self.r1, self.r2)

        with self.assertRaises(TypeError) as context:
            Rectangle()
        self.assertEqual(str(context.exception), "__init__() \
missing 2 required positional arguments: 'width' and 'height'")

    def test_invalid_dimension_type(self):
        """Test width type validation"""
        with self.assertRaises(TypeError) as context:
            Rectangle("invalid", 2)
        self.assertEqual(str(context.exception), "width must be an integer")

        with self.assertRaises(TypeError) as context:
            Rectangle(7, {})
        self.assertEqual(str(context.exception), "height must be an integer")

        with self.assertRaises(ValueError) as context:
            Rectangle(-1, 5)
        self.assertEqual(str(context.exception), "width must be > 0")

        with self.assertRaises(ValueError) as context:
            Rectangle(1, -5)
        self.assertEqual(str(context.exception), "height must be > 0")

        with self.assertRaises(TypeError) as context:
            Rectangle(1, 5, 0, [])
        self.assertEqual(str(context.exception), "y must be an integer")

        with self.assertRaises(ValueError) as context:
            Rectangle(1, 5, -2, 7)
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_width_setter(self):
        """Test width setter validation"""
        with self.assertRaises(ValueError) as context:
            self.r1.width = 0
        self.assertEqual(str(context.exception), "width must be > 0")

        with self.assertRaises(ValueError) as context:
            self.r1.width = 0
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_area(self):
        """Test area function"""
        self.assertEqual(self.r1.area(), 15)
        self.assertEqual(self.r3.area(), 20)


if __name__ == '__main__':
    unittest.main()
