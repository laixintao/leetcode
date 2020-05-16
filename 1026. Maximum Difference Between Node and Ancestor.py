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
    # find solution method
    function = [method for method in dir(s) if not method.startswith("__")][0]
    ans = getattr(s, function)(*args)
    print("ans=", ans)


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        from functools import lru_cache
        diff = 0

        @lru_cache
        def walk(node):
            nonlocal diff
            values = []
            if node.left:
                values.extend(walk(node.left))
            if node.right:
                values.extend(walk(node.right))
            if not values:
                return node.val, node.val
            _min, _max = (
                min(values),
                max(values),
            )

            diff = max(abs(_min - node.val), abs(_max - node.val), diff)
            return min(_min, node.val), max(_max, node.val)

        walk(root)
        return diff


if __name__ == "__main__":
    test("USA")
    test("flaG")
