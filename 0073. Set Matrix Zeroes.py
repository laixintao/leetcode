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
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        left_zero = False

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j == 0:
                    if matrix[i][j] == 0:
                        left_zero = True
                elif matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        print(matrix)

        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix[i])-1, -1, -1):
                if j == 0:
                    if left_zero:
                        matrix[i][0] = 0
                else:
                    if matrix[0][j] == 0 or matrix[i][0] == 0:
                        matrix[i][j] = 0

        return matrix


if __name__ == "__main__":
    test([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    test([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
    test([[1], [0]])
