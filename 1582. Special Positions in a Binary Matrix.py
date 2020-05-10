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
    def numSpecial(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0
        row_count = [0] * len(mat)
        col_count = [0] * len(mat[0])

        for row_index, row in enumerate(mat):
            for col_index, num in enumerate(row):
                row_count[row_index] += num
                col_count[col_index] += num

        count = 0

        print(f"{row_count=} {col_count=}")

        for row_index, row in enumerate(row_count):
            if row == 1:
                for col_index, col in enumerate(col_count):
                    if col == 1:
                        if mat[row_index][col_index] == 1:
                            count += 1
                            break
        return count


if __name__ == "__main__":
    test([[1, 0, 0], [0, 0, 1], [1, 0, 0]])
    test([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    test([[0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]])
    test(
        [
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1],
        ]
    )
    test(
        [
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0],
        ]
    )
