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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        temp = head
        size = 0
        while temp:
            size += 1
            temp = temp.next

        # must using a global variable (or closure)
        self.runner = head
        return self.to_bst(0, size - 1)

    def to_bst(self, left, right):
        if left > right:
            return None

        mid = (left + right) // 2
        left_node = self.to_bst(left, mid - 1)
        node = TreeNode(self.runner.val)
        self.runner = self.runner.next
        right_node = self.to_bst(mid + 1, right)

        node.left = left_node
        node.right = right_node
        return node


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.rangeSumBST(*args)
    print("ans=", ans)


if __name__ == "__main__":
    root = create_tree([10, 5, 15, 3, 7, None, 18])
    test(root, 7, 15)
