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
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        if not root.val:
            return 0

        if root.val > R:
            return self.rangeSumBST(root.left, L, R)
        if root.val < L:
            return self.rangeSumBST(root.right, L, R)
        return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.rangeSumBST(*args)
    print("ans=", ans)


if __name__ == "__main__":
    root = create_tree([10, 5, 15, 3, 7, None, 18])
    test(root, 7, 15)
