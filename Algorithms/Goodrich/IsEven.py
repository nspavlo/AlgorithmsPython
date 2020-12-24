# Write a short Python function, that takes an integer value and
# returns `True` `if` `k` is even, and `False` otherwise.
# However, your function cannot use the multiplication, modulo, or division operators.

class Solution:
    def isEven(self, k: int) -> bool:
        return not k & 1


import unittest

class TestIsEven(unittest.TestCase):
    def test_evenPositiveValue(self):
        sut = Solution().isEven(2)
        self.assertEqual(sut, True)

    def test_unevenPositiveValue(self):
        sut = Solution().isEven(3)
        self.assertEqual(sut, False)

    def test_evenZeroValue(self):
        sut = Solution().isEven(0)
        self.assertEqual(sut, True)

    def test_evenNegativeValue(self):
        sut = Solution().isEven(-2)
        self.assertEqual(sut, True)

    def test_unevenNegativeValue(self):
        sut = Solution().isEven(-1)
        self.assertEqual(sut, False)
