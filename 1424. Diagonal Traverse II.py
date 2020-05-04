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


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        from collections import defaultdict

        start_on = 0
        ans = []
        temp = defaultdict()
        for num in nums:
            for index in range(len(num)):
                temp.setdefault(index + start_on, []).append(num[index])
            start_on += 1
        index = 0
        while 1:
            row = temp.get(index)
            if not row:
                break
            ans.extend(reversed(row))
            index += 1
        return ans


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.findDiagonalOrder(*args)
    print("ans=", ans)


if __name__ == "__main__":
    test([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
