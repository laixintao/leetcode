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


def print_tree(root):
    print(root)
    print(root.left)
    print(root.right)


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
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(t) + 1)] for __ in range(len(s) + 1)]
        for row in dp:
            row[0] = 1

        for s_index in range(1, len(s) + 1):
            for t_index in range(1, len(t) + 1):
                dp[s_index][t_index] = dp[s_index - 1][t_index] + dp[s_index - 1][
                    t_index - 1
                ] * (s[s_index - 1] == t[t_index - 1])
        return dp[len(s)][len(t)]


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.numDistinct(*args)
    print("ans=", ans)


if __name__ == "__main__":
    test("babgbag", "bag")
