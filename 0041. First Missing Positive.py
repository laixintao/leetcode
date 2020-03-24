from typing import List
from collections import Counter, defaultdict
import bisect
import itertools


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        NON_EXIST = len(nums) + 1
        for index, num in enumerate(nums):
            if num <= 0 or num > len(nums):
                nums[index] = NON_EXIST
        for num in nums:
            index = abs(num)
            if index == NON_EXIST:
                continue
            nums[index - 1] = -abs(nums[index - 1])
        for index in range(0, len(nums)):
            if nums[index] > 0:
                return index + 1
        return len(nums) + 1


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.firstMissingPositive(*args)
    print("ans=", ans)


if __name__ == "__main__":
    test([1, 2, 0])
    test([3, 4, -1, 1])
    test([7, 8, 9, 11, 12])
    test([])
    test([1])
    test([1,1])
