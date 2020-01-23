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


case = 0


def test(*args):
    global case
    print(f"---case {case}---")
    case += 1
    print(f"{args=}")
    s = Solution()
    ans = s.jump(*args)
    print("ans=", ans)


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        left = 0
        right = nums[0]
        times = 1
        while right < len(nums) -1:
            times += 1
            left, right = right, max(nums[i] + i for i in range(left, right+1))
        return times


if __name__ == "__main__":
    test([2, 3, 1, 1, 4])

