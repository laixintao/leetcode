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


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.firstMissingPositive(*args)
    print("ans=", ans)


if __name__ == "__main__":
    test([1, 2, 3], [1, 2, 3])  # true
    test([1, 2], [1, None, 2])  # false
    test([1, 2, 1], [1, 1, 2])  # true
