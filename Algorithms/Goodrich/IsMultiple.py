import unittest


# Write a short Python function, that takes two integer values
# and returns `True` `if` `n` is a multiple of `m`,
# that is, `n = mi` for some integer `i`, and `False` otherwise.

class Solution:
    @staticmethod
    def is_multiple(n: int, m: int) -> bool:
        return n % m == 0


class TestIsMultiple(unittest.TestCase):
    def test_divisible_multiples(self):
        sut = Solution.is_multiple(4, 2)
        self.assertEqual(sut, True)

    def test_indivisible_multiples(self):
        sut = Solution.is_multiple(8, 3)
        self.assertEqual(sut, False)
