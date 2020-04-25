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
    def dfs_height(self, root):
        if not root:
            return -1
        left = self.dfs_height(root.left)
        if left == -1:
            return -1
        right = self.dfs_height(root.right)
        if right == -1:
            return -1
        if abs(right - left) > 1:
            return -1
        return max(left, right)

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        left = self.get_depth(root.left)
        right = self.get_depth(root.right)
        if max(right, left) - min(left, right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.zigzagLevelOrder(*args)
    print("ans=", ans)


if __name__ == "__main__":
    head = create_tree([3, 9, 20, None, None, 15, 7])
    test(head)
    head = create_tree([])
    test(head)
    head = create_tree([1])
    test(head)
