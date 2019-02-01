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
    def compare(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.compare(p.left, q.right) and self.compare(p.right, q.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.compare(root.left, root.right)


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.isSymmetric(*args)
    print("ans=", ans)


if __name__ == "__main__":
    node = create_tree([1, 2, 2, 3, 4, 4, 3])
    print(node)
    test(node)  # true
