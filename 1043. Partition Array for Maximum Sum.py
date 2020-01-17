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
    ans = s.maxSumAfterPartitioning(*args)
    # print("ans=", ans)


class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        if not K or K == 1:
            return sum(A)
        dp = [0] * len(A)
        for index, num in enumerate(A):
            possible = []
            for group in range(K):
                if index - group >= 0:
                    if index - group - 1 >= 0:
                        previous = dp[index - group - 1]
                    else:
                        previous = 0
                    possible.append(
                        previous + max(A[index - group : index + 1]) * (group + 1)
                    )

            dp[index] = max(possible)
            # print(f"{index=} {dp[index]=}")
        return dp[-1]


if __name__ == "__main__":
    test([1, 15, 7, 9, 2, 5, 10], 3)
    test([1, 15, 7, 9, 2, 5, 10], 1)
    test([1, 15, 7, 9, 2, 5, 10], 1)
