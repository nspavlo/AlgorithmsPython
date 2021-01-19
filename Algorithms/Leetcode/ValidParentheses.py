import unittest


# https://leetcode.com/problems/valid-parentheses/

def valid_parentheses(s: str) -> bool:
    parentheses = {
        "}": "{",
        "]": "[",
        ")": "("
    }

    stack = []

    for idx in range(len(s)):
        current = s[idx]

        if current in parentheses.values():
            stack.append(current)
        elif current in parentheses.keys():
            if not stack or stack.pop() != parentheses[current]:
                return False

    return not stack


class TestTwoSum(unittest.TestCase):
    def test_one_pair(self):
        sut = valid_parentheses("()")
        self.assertEqual(sut, True)

    def test_multiple_pairs(self):
        sut = valid_parentheses("()[]{}")
        self.assertEqual(sut, True)

    def test_nested_pairs(self):
        sut = valid_parentheses("{[]}")
        self.assertEqual(sut, True)

    def test_one_none_matching_pair(self):
        sut = valid_parentheses("(]")
        self.assertEqual(sut, False)

    def test_wrong_order(self):
        sut = valid_parentheses("([)]")
        self.assertEqual(sut, False)

    def test_one_sided(self):
        sut = valid_parentheses("}])")
        self.assertEqual(sut, False)
