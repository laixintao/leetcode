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
    def max_min_height(self, root):
        if not root:
            return 0, 0
        left_max, left_min = self.max_min_height(root.left)
        right_max, right_min = self.max_min_height(root.right)
        _max = max(left_max, right_max)
        _min = min(left_min, right_min)
        return _max + 1, _min + 1

    def isBalanced(self, root: TreeNode) -> bool:
        _max, _min = self.max_min_height(root)
        if _max - _min <= 1:
            return True
        return False


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
