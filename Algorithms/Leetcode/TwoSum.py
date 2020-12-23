# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


import unittest

class TestTwoSum(unittest.TestCase):
    def test_nine(self):
        sut = Solution().twoSum([2, 7, 11, 15], 9)
        self.assertEqual(sut, [0, 1])

    def test_six(self):
        sut = Solution().twoSum([3, 2, 4], 6)
        self.assertEqual(sut, [1, 2])