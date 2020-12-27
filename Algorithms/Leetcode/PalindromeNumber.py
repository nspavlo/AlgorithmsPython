import unittest


# https://leetcode.com/problems/palindrome-number/

def is_palindrome(x: int) -> bool:
    number = x
    reverse_number = 0

    while number > 0:
        # calculate last digit (23 -> 3)
        digit = number % 10

        # append last digit to reverseNumber (0 + 3 -> 3), (3 + 2 -> 32)
        reverse_number = (reverse_number * 10) + digit

        # remove last digit from number (1.2 -> 1)
        number = int(number / 10)

    return reverse_number == x


class TestIsPalindrome(unittest.TestCase):
    def test_one_hundred_and_twenty_one(self):
        sut = is_palindrome(121)
        self.assertEqual(sut, True)

    def test_negative_one_hundred_and_twenty_one(self):
        sut = is_palindrome(-121)
        self.assertEqual(sut, False)

    def test_ten(self):
        sut = is_palindrome(10)
        self.assertEqual(sut, False)

    def test_zero(self):
        sut = is_palindrome(0)
        self.assertEqual(sut, True)
