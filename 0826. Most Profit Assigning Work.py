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
    # find solution method
    function = [method for method in dir(s) if not method.startswith("__")][0]
    ans = getattr(s, function)(*args)
    print("ans=", ans)


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        """ Two pointers"""
        jobs = sorted(zip(difficulty, profit))
        job_index = ans = best = 0
        for aility in sorted(worker):
            while job_index < len(worker) and jobs[job_index][0] <= aility:
                best = max(jobs[job_index][1],best)
                job_index += 1
            ans += best
        return ans



if __name__ == "__main__":

    test([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7])
    test([85, 47, 57], [24, 66, 99], [40, 25, 25])
    test([13, 37, 58], [4, 90, 96], [34, 73, 45])
