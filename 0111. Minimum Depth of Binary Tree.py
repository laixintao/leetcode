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
    def minDepth(self, root: TreeNode) -> int:
        stack = [root]
        ans = 1
        while stack:
            next_level = []
            for node in stack:
                print(node.val, node.left.val, node.right.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                if node.left is None and node.right is None:
                    print(node.val)
                    return ans
            stack = next_level


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.minDepth(*args)
    print("ans=", ans)


if __name__ == "__main__":
    root = create_tree([3, 9, 20, None, None, 15, 7])
    test(root)
