from typing import List
from collections import Counter, defaultdict
import bisect
import itertools


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f"[{self.val}]({self.left}, {self.right})"


def create_tree(values):
    root = TreeNode(values.pop(0))
    roots = [root]
    while values:
        left, right = values.pop(0), values.pop(0)
        node = roots.pop(0)
        node.left = TreeNode(left)
        node.right = TreeNode(right)
        roots.extend([node.left, node.right])
    return root


class Solution:
    def do(self, digits: List, index):
        if index == -1:
            digits.insert(0, 1)
            return
        ans = digits[index] + 1
        if ans < 10:
            digits[index] = ans
            return

        digits[index] = 0
        self.do(digits, index - 1)

    def plusOne(self, digits: List[int]) -> List[int]:
        self.do(digits, len(digits) - 1)
        return digits


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.plusOne(*args)
    print("ans=", ans)


if __name__ == "__main__":
    test([1,2,3])
    test([1,2,9])
    test([9,9,9])
