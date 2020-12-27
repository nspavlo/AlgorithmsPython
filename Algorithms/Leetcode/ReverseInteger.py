import unittest


# https://leetcode.com/problems/reverse-integer/

def reverse(x: int) -> int:
    i = str(abs(x))
    j = int(i[::-1])

    # limit to 32 bit integer
    if j > 0x7FFFFFFF:
        return 0

    if x < 0:
        return j * -1
    else:
        return j


class TestReverseInteger(unittest.TestCase):
    def test_overflow(self):
        sut = reverse(1534236469)
        self.assertEqual(sut, 0)

    def test_one_hundred_and_twenty_three(self):
        sut = reverse(123)
        self.assertEqual(sut, 321)

    def test_minus_one_hundred_and_twenty_three(self):
        sut = reverse(-123)
        self.assertEqual(sut, -321)

    def test_zero(self):
        sut = reverse(0)
        self.assertEqual(sut, 0)
