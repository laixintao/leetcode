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


case = 0


def test(*args):
    global case
    print(f"---case {case}---")
    case += 1
    print(f"{args=}")
    s = Solution()
    ans = s.isMatch(*args)
    print("ans=", ans)


class Solution:
    """动态规划解决"""

    def isMatch(self, s, p):
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(len(p) + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                dp[i][j] = (p[j - 1] in ("?", "*", s[i - 1]) and dp[i - 1][j - 1]) or (
                    p[j - 1] == "*" and (dp[i][j - 1] or dp[i - 1][j])
                )

        return dp[len(s)][len(p)]


if __name__ == "__main__":
    test("aa", "a")
    test("aa", "a*")
    test("abc", "abx?c")
    test("acdcb", "a*c?b")
    test("aa", "*")
    test("acdcb", "a*c?b")
    test("", "?")
