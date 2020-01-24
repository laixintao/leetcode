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
    ans = s.merge(*args)
    print("ans=", ans)


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        from bisect import bisect_left

        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = 0
        right = m
        while nums2:
            num = nums2.pop(0)
            left = bisect_left( nums1,num, left, right)
            right += 1
            nums1.insert(left, num)
        nums1[n+m:] = []
        return nums1


if __name__ == "__main__":
    test([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)

