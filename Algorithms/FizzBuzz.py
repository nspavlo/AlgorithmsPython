import unittest


def fizzbuzz(n: int) -> str:
    if n % 15 == 0:
        return "fizz buzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)


class TestFizzBuzz(unittest.TestCase):
    def test_one(self):
        sut = fizzbuzz(1)
        self.assertEqual(sut, "1")

    def test_divisible_by_three(self):
        sut = fizzbuzz(3)
        self.assertEqual(sut, "fizz")

    def test_divisible_by_five(self):
        sut = fizzbuzz(5)
        self.assertEqual(sut, "buzz")

    def test_divisible_by_fifteen(self):
        sut = fizzbuzz(15)
        self.assertEqual(sut, "fizz buzz")
