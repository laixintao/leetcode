from typing import List
from collections import Counter, defaultdict
import bisect
import itertools


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        solutions = [set() for _ in range(target+1)]
        solutions[0].add(())
        for num in reversed(candidates):
            for to_update in range(target, num - 1, -1):
                for solution in solutions[to_update - num]:
                   solutions[to_update].add(solution + (num,))
        return list(solutions[target])


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.combinationSum2(*args)
    print("ans=", ans)


if __name__ == "__main__":
    test([2, 3, 6, 7], 7)
    test([2, 3, 5], 8)
    test([2, 5, 2, 1, 2], 5)
