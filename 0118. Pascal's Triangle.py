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
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        ans = [[1]]
        for index in range(1, numRows):
            row = [1]
            for x in range(1, index):
                print(f"{index=} {x=} {ans=}")
                row.append(ans[index - 1][x] + ans[index - 1][x - 1])
            row.append(1)
            ans.append(row)

        return ans


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.generate(*args)
    print("ans=", ans)


if __name__ == "__main__":
    test(1)
    test(3)
