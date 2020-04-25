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
    def depth(self, root, current):
        if not root:
            return current
        return max(
            self.depth(root.left, current + 1), self.depth(root.right, current + 1)
        )

    def printTree(self, root: TreeNode) -> List[List[str]]:

        tree_rows = []
        stack = [root]
        while stack:
            current_values = []
            next_level = []
            for node in stack:
                if node is None:
                    current_values.append(None)
                else:
                    current_values.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
            stack = next_level
            tree_rows.append(current_values)

        # draw
        height = self.depth(root, 0)
        max_col = 2 ** height - 1
        ans = [["" for _ in range(max_col)] for __ in range(height)]
        for index, row in enumerate(tree_rows):
            left_padding = 2 ** (height - index - 1) - 1
            space = 2 ** (height - index) - 1
            # print(row)
            for col, value in enumerate(row):
                if value is not None:
                    position = left_padding + col * space + col
                    # print(f"{value=} {left_padding=} {space=} {col=}")
                    ans[index][position] = str(value)

        return ans


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
