from typing import List
from collections import Counter
import bisect
import itertools


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [[] for x in range(9)]
        rows = board
        columns = [[] for x in range(9)]

        for row in board:
            for index, number in enumerate(row):
                columns[index].append(number)

        for row_number, row in enumerate(board):
            for col_number, num in enumerate(row):
                boxes[3 * (row_number // 3) + (col_number // 3)].append(num)

        for unit in itertools.chain(boxes, rows, columns):
            if len(set(unit)) + unit.count(".") - 1 != len(unit):
                return False
        return True


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.isValidSudoku(*args)
    print("ans=", ans)


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

    test(
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
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
