# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = x
        reverseNumber = 0

        while number > 0:
            # calculate last digit (23 -> 3)
            digit = number % 10

            # append last digit to reverseNumber (0 + 3 -> 3), (3 + 2 -> 32)
            reverseNumber = (reverseNumber * 10) + digit

            # remove last digit from number (1.2 -> 1)
            number = int(number / 10)

        return reverseNumber == x


import unittest

class TestIsPalindrome(unittest.TestCase):
    def test_oneHundredAndTwentyOne(self):
        sut = Solution().isPalindrome(121)
        self.assertEqual(sut, True)

    def test_negative(self):
        sut = Solution().isPalindrome(-121)
        self.assertEqual(sut, False)

    def test_ten(self):
        sut = Solution().isPalindrome(10)
        self.assertEqual(sut, False)

    def test_zero(self):
        sut = Solution().isPalindrome(0)
        self.assertEqual(sut, True)