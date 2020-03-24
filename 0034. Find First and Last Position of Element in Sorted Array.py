from typing import List


from collections import Counter
import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        insert_position = bisect.bisect_left(nums, target)
        if insert_position >= len(nums) or nums[insert_position] != target:
            return [-1, -1]
        left = insert_position
        while insert_position < len(nums) and nums[insert_position] == target:
            insert_position += 1
        return [left, insert_position-1]
        

def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.searchRange(*args)
    print("ans=", ans)


if __name__ == "__main__":
    test([5,7,7,8,8,10], 8)
    test([5,7,7,8,8,10], 6)
    test([], 0)
    test([1], 0)
    test([1,2], 0)
    test([2,2], 3)
