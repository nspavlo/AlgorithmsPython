import unittest


# https://leetcode.com/problems/longest-common-prefix/

def contains_common_prefix(strs: [str], prefix: str) -> bool:
    for str in strs:
        if not str.startswith(prefix):
            return False

    return True


def longest_common_prefix(strs: [str]) -> str:
    # check for empty list
    if not strs:
        return ""

    # raises index error when list is empty
    prefix = strs.pop(0)

    # reduce string by one and compare for common prefix
    while prefix:
        if contains_common_prefix(strs, prefix):
            return prefix
        else:
            prefix = prefix[:-1]

    # explicitly return empty string here
    return ""


class TestLongestCommonPrefix(unittest.TestCase):
    def test_items_with_common_prefix(self):
        sut = longest_common_prefix(["flower", "flow", "flight"])
        self.assertEqual(sut, "fl")

    def test_items_without_common_prefix(self):
        sut = longest_common_prefix(["dog", "race car", "car"])
        self.assertEqual(sut, "")

    def test_empty_list(self):
        sut = longest_common_prefix([])
        self.assertEqual(sut, "")
