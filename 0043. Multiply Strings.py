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
    ans = s.trap(*args)
    print("ans=", ans)


class Solution:
    def trap(self, height: List[int]) -> int:
        dp = [0] * (len(height) + 1)
        max_height = [0] * (len(height) + 1)

        for index in range(1, len(height) + 1):
            current = height[index - 1]

            for _start in range(index - 2, 0, -1):
                if height[_start] >= current:
                    start = _start
                    break
            else:
                start = max_height[index - 1]

            latter = 0
            limit = min(height[start], current)
            for new in range(start + 1, index - 1):
                latter += (limit - height[new])

            dp[index] = dp[start+1] + latter

            print(f"{index=} {current=} {start=} {dp[index]=}")

            if height[max_height[index - 1]] <= current:
                max_height[index] = index - 1
            else:
                max_height[index] = max_height[index - 1]

        print(max_height)
        return dp[len(height)]


if __name__ == "__main__":
    test([1, 0, 2])
    test([0, 1, 0, 2])
    test([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    test([])
