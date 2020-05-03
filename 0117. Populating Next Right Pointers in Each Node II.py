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
    def connect(self, root):
        if not root:
            return None
        next_level = root
        current = None
        while 1:
            next_level = None
            current = next_level
            to_change = None
            while current:
                if current.left:
                    if to_change:
                        to_change.next = current.left
                    else:
                        next_level = current.left
                    to_change = current.left
                if current.right:
                    if to_change:
                        to_change.next = current.right
                    else:
                        next_level = current.right
                    to_change = current.right
                current = current.next
            if not next_level:
                break
        return root


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.numDistinct(*args)
    print("ans=", ans)


if __name__ == "__main__":
    test("babgbag", "bag")
