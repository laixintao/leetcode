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


class Solution:
    def _flatten(self, root, nodes):
        if root is None or root.val is None:
            return
        if root and root.val:
            nodes.append(root)
        self._flatten(root.left, nodes)
        self._flatten(root.right, nodes)

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        self._flatten(root, nodes)
        print(nodes)
        for index in range(len(nodes) - 1):
            nodes[index].right = nodes[index + 1]
            nodes[index].left = None
        nodes[index + 1].left = nodes[index + 1].right = None


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.flatten(*args)
    print("ans=", ans)


if __name__ == "__main__":
    root = create_tree([1, 2, 5, 3, 4, None, 6])
    test(root)
