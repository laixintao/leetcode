from typing import List
from collections import Counter, defaultdict
import bisect
import itertools


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = defaultdict(list)
        solutions[0] = [[]]
        for num in candidates:
            for to_update in range(num, target + 1):
                for solution in solutions[to_update - num]:
                    solutions[to_update].append(solution + [num])
        return solutions[target]


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.combinationSum(*args)
    print("ans=", ans)


if __name__ == "__main__":
    test([2, 3, 6, 7], 7)
    test([2, 3, 5], 8)
