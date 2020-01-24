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
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end = m+n-1
        while m-1>=0 and n-1>=0:
            if nums1[m-1] < nums2[n-1]:
                nums1[end] = nums2[n-1]
                n-=1
            else:
                nums1[end] = nums1[m-1]
                m-=1
            end -= 1
        print(nums1)
        if n-1>=0:
            nums1[0:n] = nums2[0:n]
        return nums1



if __name__ == "__main__":
    test([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    test([0], 0, [1], 1)

