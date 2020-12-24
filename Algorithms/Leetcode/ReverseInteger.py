# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        i = str(abs(x))
        j = int(i[::-1])

        # limit to 32 bit integer
        if j > 0x7FFFFFFF:
            return 0

        if x < 0:
            return j * -1
        else:
            return j


import unittest

class TestReverseInteger(unittest.TestCase):
    def test_overflow(self):
        sut = Solution().reverse(1534236469)
        self.assertEqual(sut, 0)

    def test_oneHundredAndTwentyThree(self):
        sut = Solution().reverse(123)
        self.assertEqual(sut, 321)

    def test_minusOneHundredAndTwentyThree(self):
        sut = Solution().reverse(-123)
        self.assertEqual(sut, -321)

    def test_zero(self):
        sut = Solution().reverse(0)
        self.assertEqual(sut, 0)
