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
    def pancakeSort(self, A: List[int]) -> List[int]:
        ans = []
        for last in range(len(A), 0, -1):
            index = A.index(last)
            ans.extend([index+1, last])
            A = A[:index:-1] + A[:index]
        return ans


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.pancakeSort(*args)
    print("ans=", ans)


if __name__ == "__main__":
    test([3,2,4,1])
