import unittest

from fraction.model.fraction import Fraction


class TestFractionClass(unittest.TestCase):
    def test_can_create_str_from_fraction(self):
        frac = Fraction(p=2, q=4)
        self.assertEqual(str(frac), '2/4')

    def test_mul_fraction(self):
        f0 = Fraction(1, 2)
        f1 = Fraction(0, 3)
        self.assertTrue((f0 * f2).is_equal(0, 1))