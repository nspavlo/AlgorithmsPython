# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def containsCommonPrefix(self, strs: [str], prefix: str) -> bool:
        for str in strs:
            if not str.startswith(prefix):
                return False

        return True

    def longestCommonPrefix(self, strs: [str]) -> str:
        # check for empty list
        if not strs: 
            return ""

        # raises index error when list is empty
        prefix = strs.pop(0)

        # reduce string by one and compare for common prefix
        while prefix:
            if self.containsCommonPrefix(strs, prefix):
                return prefix
            else:
                prefix = prefix[:-1]

        # explicitly return empty string here
        return ""


import unittest

class TestLongestCommonPrefix(unittest.TestCase):
    def test_itemsWithCommonPrefix(self):
        sut = Solution().longestCommonPrefix(["flower", "flow", "flight"])
        self.assertEqual(sut, "fl")

    def test_itemsWithoutCommonPrefix(self):
        sut = Solution().longestCommonPrefix(["dog", "racecar", "car"])
        self.assertEqual(sut, "")

    def test_emptyList(self):
        sut = Solution().longestCommonPrefix([])
        self.assertEqual(sut, "")