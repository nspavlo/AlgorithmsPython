class Solution:
    def romanToInt(self, s: str) -> int:
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


import unittest

class TestRomanToInt(unittest.TestCase):
    def test_three(self):
        sut = Solution().romanToInt("III")
        self.assertEqual(sut, 3)

    def test_four(self):
        sut = Solution().romanToInt("IV")
        self.assertEqual(sut, 4)

    def test_nine(self):
        sut = Solution().romanToInt("IX")
        self.assertEqual(sut, 9)

    def test_fiftyEight(self):
        sut = Solution().romanToInt("LVIII")
        self.assertEqual(sut, 58)

    def test_oneThousandNineHundredAndNinetyFour(self):
        sut = Solution().romanToInt("MCMXCIV")
        self.assertEqual(sut, 1994)