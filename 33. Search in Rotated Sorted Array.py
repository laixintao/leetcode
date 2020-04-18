from typing import List


from collections import Counter
import bisect

class Solution:
    def binary_search(self, nums, target, start, end):
        """
        start end are included
        """
        if start > end:
            return -1
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        if start == end:
            return -1

        middle = (end + start) // 2
        if nums[start] > nums[end]:
            found_in_left = self.binary_search(nums, target, start, middle)
            if found_in_left != -1:
                return found_in_left
            found_in_right = self.binary_search(nums, target, middle+1, end)
            if found_in_right != -1:
                return found_in_right
        else: # sorted
            if nums[middle] >= target:
                found_in_left = self.binary_search(nums, target, start, middle)
                if found_in_left != -1:
                    return found_in_left
            if nums[middle] < target:
                found_in_right = self.binary_search(nums, target, middle+1, end)
                if found_in_right != -1:
                    return found_in_right
            return -1
        return -1


    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums)-1)


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.search(*args)
    print("ans=", ans)


if __name__ == "__main__":
    test([4,5,6,7,0,1,2], 0)
    test([4,5,6,7,0,1,2], 3)
    test([], 3)
