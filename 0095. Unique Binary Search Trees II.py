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
    def generate(self, left, right):
        if left == right:
            return None
        result = []
        for root in range(left, right):
            for l in self.generate(left,root) or [None]:
                for r in self.generate(root+1, right) or [None]:
                    node = TreeNode(root)
                    node.left = l
                    node.right = r
                    result.append(node)
        return result


    def generateTrees(self, n: int) -> List[TreeNode]:
        if  n==0:
            return [[]]
        return self.generate(1, n+1)

        


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.isSymmetric(*args)
    print("ans=", ans)


if __name__ == "__main__":
    node = create_tree([1, 2, 2, 3, 4, 4, 3])
    print(node)
    test(node)  # true
