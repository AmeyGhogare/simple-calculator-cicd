
import unittest
from calculator import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(50, 20), 70)

    def test_subtract(self):
        self.assertEqual(subtract(50, 20), 30)

    def test_multiply(self):
        self.assertEqual(multiply(50, 20), 1000)

    def test_divide(self):
        self.assertEqual(divide(50, 10), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(50, 0)


if __name__ == "__main__":
    unittest.main()
