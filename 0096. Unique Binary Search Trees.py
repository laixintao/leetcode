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
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for index in range(2, n + 1):
            for root in range(index + 1):
                dp[index] += dp[root-1] * dp[index - root]
        return dp[n]


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.numTrees(*args)
    print("ans=", ans)


if __name__ == "__main__":
    test(3)  # true
