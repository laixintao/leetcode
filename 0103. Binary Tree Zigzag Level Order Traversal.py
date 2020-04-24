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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        ltr = True
        ans = []
        while stack:
            next_level = []
            ans_level = []
            while 1:
                if not stack:
                    ltr = not ltr
                    break
                node = stack.pop()
                if not node:
                    continue
                if node.val is not None:
                    ans_level.append(node.val)
                if ltr:
                    next_level.extend([node.left, node.right])
                else:
                    next_level.extend([node.right, node.left])
            stack = next_level
            if ans_level:
                ans.append(ans_level)
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
