import unittest


# https://leetcode.com/problems/roman-to-integer/

def roman_to_int(s: str) -> int:
    mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    otp = 0
    tmp = 0

    for c in s:
        val = mapping.get(c)

        # roman numerals are usually written largest to smallest (XXVII)
        # detect subtraction (IV)
        if tmp < val:
            # subtract from value and otp
            tmp = val - (tmp * 2)
        else:
            # add w/o change
            tmp = val

        otp += tmp

    return otp


class TestRomanToInt(unittest.TestCase):
    def test_three(self):
        sut = roman_to_int("III")
        self.assertEqual(sut, 3)

    def test_four(self):
        sut = roman_to_int("IV")
        self.assertEqual(sut, 4)

    def test_nine(self):
        sut = roman_to_int("IX")
        self.assertEqual(sut, 9)

    def test_fifty_eight(self):
        sut = roman_to_int("LVIII")
        self.assertEqual(sut, 58)

    def test_one_thousand_nine_hundred_and_ninety_four(self):
        sut = roman_to_int("MCMXCIV")
        self.assertEqual(sut, 1994)
