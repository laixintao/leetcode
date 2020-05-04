from typing import List
from collections import Counter, defaultdict
import bisect
import itertools


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


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f"[{self.val}]({self.left}, {self.right})"

    def __repr__(self):
        return f"TreeNode({self.val})"


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        for index in range(1, len(s)):
            left = s[:index]
            right = s[index:]
            # print(f"{left=} {right=}")
            temp = sum("0" == char for char in left) + sum(
                "1" == char for char in right
            )
            if temp > score:
                score = temp
        return score


def test(*args):
    # print(f"{args=}")
    s = Solution()
    ans = s.maxScore(*args)
    # print("ans=", ans)


if __name__ == "__main__":
    test("011101")
    test("00111")
    test("01")
