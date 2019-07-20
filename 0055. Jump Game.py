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
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        index = len(nums) - 2
        last_index = len(nums) - 1
        while index > 0:
            steps = nums[index]
            reach = steps + index
            if reach >= last_index:
                last_index = index
            index -= 1
        return nums[0] >= last_index


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.canJump(*args)
    print("ans=", ans)


if __name__ == "__main__":
    test([2, 3, 1, 1, 4])
    test([3, 2, 1, 0, 4])
