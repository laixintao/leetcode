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
    # print(f"---case {case}---")
    case += 1
    # print(f"{args=}")
    s = Solution()
    ans = s.singleNonDuplicate(*args)
    # print("ans=", ans)


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # print(nums)
        if len(nums) == 1:
            return nums[0]
        left_end = len(nums) // 2
        if not left_end & 1:
            left_end += 1
        # print(left_end)
        if nums[left_end] == nums[left_end - 1]:
            return self.singleNonDuplicate(nums[left_end + 1 :])
        return self.singleNonDuplicate(nums[:left_end])


if __name__ == "__main__":
    test([1, 1, 2])
    test([1, 1, 2, 3, 3, 4, 4, 8, 8])
