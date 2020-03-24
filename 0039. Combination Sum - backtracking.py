from typing import List
from collections import Counter
import bisect
import itertools


class Solution:
    def solve(self, found, candidates, target, solutions):
        count = 0
        num = candidates.pop()
        while 1:
            new_target = target - count * num
            if new_target < 0:
                break
            elif new_target == 0:
                solutions.append(found + [num] * count)
                break
            else:
                if candidates:
                    self.solve(found + [num] * count, candidates, new_target, solutions)
                count += 1
        candidates.append(num)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = []
        self.solve([], candidates, target, solutions)
        return solutions


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.combinationSum(*args)
    print("ans=", ans)


if __name__ == "__main__":
    test([2, 3, 6, 7], 7)
    test([2, 3, 5], 8)
