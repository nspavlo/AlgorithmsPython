# Write a short Python function, that takes two integer values
# and returns `True` `if` `n` is a multiple of `m`,
# that is, `n = mi` for some integer `i`, and `False` otherwise.

class Solution:
    def isMultiple(self, n: int, m: int) -> bool:
        return n % m == 0


import unittest

class TestIsMultiple(unittest.TestCase):
    def test_divisibleMultiples(self):
        sut = Solution().isMultiple(4, 2)
        self.assertEqual(sut, True)

    def test_indivisibleMultiples(self):
        sut = Solution().isMultiple(8, 3)
        self.assertEqual(sut, False)
