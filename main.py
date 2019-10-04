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
    ans = s.uniquePaths(*args)
    print("ans=", ans)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        possible = [[1] * (n + 1) for _ in range(m + 1)]

        for _m in range(2, m+1):
            for _n in range(2, n+1):
                possible[_m][_n] = sum(possible[_m-down][_n-1] for down in range(_m))
                print(f"{_m=} {_n=} {possible[_m][_n]=}")

        return possible[m][n]


if __name__ == "__main__":
    test(2, 2)
    test(3, 2)
    test(7, 3)

