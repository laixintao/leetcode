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
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints)
        score = 0
        score = cache = sum(cardPoints[len(cardPoints) - k :])
        for index in range(0, k):
            cache = cache + cardPoints[index] - cardPoints[len(cardPoints) - k + index]
            score = max(score, cache)
        return score


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.maxScore(*args)
    print("ans=", ans)


if __name__ == "__main__":
    test([1, 2, 3, 4, 5, 6, 1], 3)
    test([2, 2, 2], 2)
    test([9, 7, 7, 9, 7, 7, 9], 7)
