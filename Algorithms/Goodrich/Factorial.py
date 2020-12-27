import unittest


def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


class TestFactorial(unittest.TestCase):
    def test_one(self):
        sut = factorial(1)
        self.assertEqual(sut, 1)

    def test_for(self):
        sut = factorial(4)
        self.assertEqual(sut, 24)
