import unittest


# Number of operations for computing factorial(n) is O(n),
# as there are n + 1 activations, each of which accounts for O(1) operations.

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
