from typing import List
from collections import Counter
import bisect
import itertools


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    for try_number in range(1, 10):
                        try_number = str(try_number)
                        if self.is_valid(board, row, col, try_number):
                            board[row][col] = str(try_number)
                            if self.solveSudoku(board):
                                return True
                            board[row][col] = "."
                    return False
        return True

    def is_valid(self, board, row, col, num):
        for row_index in range(9):
            for col_index in range(9):
                if row_index == row and board[row_index][col_index] == num:
                    return False
                if col_index == col and board[row_index][col_index] == num:
                    return False

                if ((row_index // 3) * 3 + col_index // 3) == (
                    (row // 3) * 3 + col // 3
                ) and board[row_index][col_index] == num:
                    return False
        return True


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.solveSudoku(*args)
    print("ans=", ans)
    print(args)


if __name__ == "__main__":
    test(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
