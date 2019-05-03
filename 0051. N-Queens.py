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
    def play(self, board, row, n, ans):

        if row == n:
            temp = []
            for row_index in range(n):
                line = []
                for col_index in range(n):
                    if board[row_index][col_index]:
                        line.append("Q")
                    else:
                        line.append(".")
                temp.append("".join(line))
            ans.append(temp)
            return

        for col in range(n):
            move_is_legal = True
            if row > 0:
                for row_i in range(0, row):
                    if board[row_i][col]:
                        move_is_legal = False
                        break
                    right_up = (row - row_i) + col
                    if 0 <= right_up < n and board[row_i][right_up]:
                        move_is_legal = False
                        break
                    left_up = col - (row - row_i)
                    if 0 <= left_up < n and board[row_i][left_up]:
                        move_is_legal = False
                        break

            if move_is_legal:
                board[row][col] = True
                self.play(board, row + 1, n, ans)
                board[row][col] = False
        return ans

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[False for x in range(n)] for __ in range(n)]
        ans = []
        return self.play(board, 0, n, ans)


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.solveNQueens(*args)
    print("ans=", ans)


if __name__ == "__main__":
    test(4)
