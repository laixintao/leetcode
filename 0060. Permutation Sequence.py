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
    ans = s.getPermutation(*args)
    print("ans=", ans)


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math

        ans, nums = "", list(range(1, n + 1))
        # nums start from the first one, not zero one
        k -= 1

        while n:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            ans += str(nums.pop(index))
        return ans


if __name__ == "__main__":
    test(3, 3)  # 213
    test(4, 9)  # 2314
    test(4, 3)  # 1324
