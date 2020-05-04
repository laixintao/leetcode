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
    ans = s.maxSlidingWindow(*args)
    print("ans=", ans)


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import collections

        indexes_window = collections.deque()
        index = 0
        ans = []
        while index < len(nums):
            if indexes_window and indexes_window[0] <= index - k:
                indexes_window.popleft()

            while indexes_window and nums[indexes_window[-1]] <= nums[index]:
                indexes_window.pop()

            indexes_window.append(index)
            print(indexes_window)

            if index >= k - 1:
                ans.append(nums[indexes_window[0]])

            index += 1
        return ans


if __name__ == "__main__":
    test([1, 3, -1, -3, 5, 3, 6, 7], 3)
    test([7, 2, 4], 2)
