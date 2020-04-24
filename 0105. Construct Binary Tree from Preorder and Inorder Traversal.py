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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        head = preorder[0]
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        for count in len(inorder):
            if inorder[count] == head:
                root = TreeNode(head)
                root.left = self.buildTree(preorder[1 : count + 1], inorder[0:count])
                root.right = self.buildTree(preorder[count + 1 :], inorder[count + 1 :])
                return root


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
