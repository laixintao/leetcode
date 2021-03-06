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


from functools import lru_cache
class Solution:
    @lru_cache
    def minDistance(self, word1: str, word2: str) -> int:

        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        if word1[-1] == word2[-1]:
            return self.minDistance(word1[:-1], word2[:-1])
        return 1 + min(
            self.minDistance(word1, word2[:-1]),  # insert
            self.minDistance(word1[:-1], word2[:-1]),  # replase
            self.minDistance(word1[:-1], word2),
        )  # delete


if __name__ == "__main__":
    test("horse", "ros")
    test("intention", "execution")
    test("dinitrophenylhydrazine", "benzalphenylhydrazone")
