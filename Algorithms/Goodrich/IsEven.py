import unittest


# Write a short Python function, that takes an integer value and
# returns `True` `if` `k` is even, and `False` otherwise.
# However, your function cannot use the multiplication, modulo, or division operators.

class Solution:
    @staticmethod
    def is_even(k: int) -> bool:
        return not k & 1


class TestIsEven(unittest.TestCase):
    def test_even_positive_value(self):
        sut = Solution.is_even(2)
        self.assertEqual(sut, True)

    def test_uneven_positive_value(self):
        sut = Solution.is_even(3)
        self.assertEqual(sut, False)

    def test_even_zero_value(self):
        sut = Solution.is_even(0)
        self.assertEqual(sut, True)

    def test_even_negative_value(self):
        sut = Solution.is_even(-2)
        self.assertEqual(sut, True)

    def test_uneven_negative_value(self):
        sut = Solution.is_even(-1)
        self.assertEqual(sut, False)
