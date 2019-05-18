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
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        order = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        ]
        row = len(matrix)
        col = len(matrix[0])
        count_using_row = True
        ans = []
        row_index, col_index = 0, -1
        for current_order in itertools.cycle(order):
            if count_using_row:
                count = col
                row -= 1
            else:
                count = row
                col -= 1

            count_using_row = not count_using_row
            # print(f"{count=} {current_order=} {row=} {col=}")
            if not count:
                break
            while count > 0:
                row_index += current_order[0]
                col_index += current_order[1]
                # print(f"{row_index=} {col_index=}")
                ans.append(matrix[row_index][col_index])
                count -= 1
        return ans


def test(*args):
    # print(f"{args=}")
    s = Solution()
    ans = s.spiralOrder(*args)
    # print("ans=", ans)


if __name__ == "__main__":
    test([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    test([[1, 2, 3]])
    test([[]])
