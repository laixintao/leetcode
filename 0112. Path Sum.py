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
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return 0
        stack = [root]
        sums = [root.val]
        while stack:
            next_level = []
            next_sums = []
            for node, node_sum in zip(stack, sums):
                if node_sum + node.val == sum:
                    return True

                if node.left:
                    next_level.append(node.left)
                    next_sums.append(node_sum + node.val)
                if node.right:
                    next_level.append(node.right)
                    next_sums.append(node_sum + node.val)
            stack = next_level
            sums = next_sums

        return False


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.minDepth(*args)
    print("ans=", ans)


if __name__ == "__main__":
    root = create_tree([3, 9, 20, None, None, 15, 7])
    test(root)
