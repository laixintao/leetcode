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


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
        )


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.firstMissingPositive(*args)
    print("ans=", ans)


if __name__ == "__main__":
    test([1, 2, 3], [1, 2, 3])  # true
    test([1, 2], [1, None, 2])  # false
    test([1, 2, 1], [1, 1, 2])  # true
