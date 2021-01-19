import unittest


# The binary search algorithm runs in O(logn) time for a sorted
# sequence with n elements.

def binary_search(data, target, low, high) -> int:
    if low > high:
        return None
    else:
        mid = (low + high) // 2

        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


class TestBinarySearch(unittest.TestCase):
    def test_one_item(self):
        sut = binary_search([0], 0, 0, 1)
        self.assertEqual(sut, 0)

    def test_large_list(self):
        sut = binary_search([1, 2, 3, 4, 5, 6, 7, 18, 19, 100], 18, 0, 9)
        self.assertEqual(sut, 7)
