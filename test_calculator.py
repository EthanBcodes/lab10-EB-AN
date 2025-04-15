# https://github.com/EthanBcodes/lab10-EB-AN
# Partner 1: Ethan Bond
# Partner 2: An Ngo

import unittest
from calculator import div, logarithm, hypotenuse, square_root


class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 5), 3)
        self.assertEqual(add(0, 7), 7)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(7, 0), 7)

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self):
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(5, 20), 4)
        self.assertAlmostEqual(div(3, 10), 10 / 3, places=5)

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)

    def test_logarithm(self):
        self.assertEqual(log(2, 8), 3)
        self.assertEqual(log(10, 1), 0)
        with self.assertRaises(ValueError):
            log(10, -5)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 10)

    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(1, 1), 2 ** 0.5)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(0), 0.0)
        with self.assertRaises(ValueError):
            square_root(-1)


if __name__ == "__main__":
    unittest.main()
