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
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return None
        x = nums[0]
        for num in nums[1:]:
            x ^= num
        return x


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.singleNumber(*args)
    print("ans=", ans)


if __name__ == "__main__":
    test([2, 2, 1])
    test([4, 1, 2, 1, 2])
