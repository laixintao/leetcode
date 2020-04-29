from typing import List
from collections import Counter, defaultdict
import bisect
import itertools


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f"[{self.val}]({self.left}, {self.right})"


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


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for __ in range(n)]
        order_index = row = col = 0
        count = 1
        order = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while count <= n ** 2:
            matrix[row][col] = count
            print(f"{row=} {col=} {count=}")
            next_row, next_col = order[order_index]
            if 0 <= row + next_row < n and 0 <= next_col + col < n and matrix[row+next_row][col+next_col] == 0:
                pass
            else:
                order_index += 1
                if order_index == 4:
                    order_index = 0

            next_row, next_col = order[order_index]
            row += next_row
            col += next_col
            count += 1
        return matrix


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.generateMatrix(*args)
    print("ans=", ans)


if __name__ == "__main__":
    test(2)
    test(3)
