from typing import List


class Solution:
    def findMedianSingleArray(self, nums):
        print(f"{nums=}")
        middle = len(nums) // 2
        r = len(nums) % 2
        if r == 0:
            return (nums[middle - 1] + nums[middle]) / 2
        return nums[middle ]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = l2 = 0
        r1 = len(nums1) - 1
        r2 = len(nums2) - 1

        while 1:
            if l1 > r1:  # left run out
                return self.findMedianSingleArray(nums2[l2 : r2 + 1])
            if l2 > r2:  # right run out
                return self.findMedianSingleArray(nums1[l1 : r1 + 1])
            if l1 == r1 and l2 == r2 and len(nums1 + nums2) % 2 ==0:
                return (nums1[l1] + nums2[l2]) / 2
            print(f"start {l1=} {l2=} {r1=} {r2=}")
            # smaller one moves to right
            if nums1[l1] < nums2[l2]:
                l1 += 1
            else:
                l2 += 1

            # bigger one moves to left
            if nums1[r1] < nums2[r2]:
                r2 -= 1
            else:
                r1 -= 1
            print(f"end {l1=} {l2=} {r1=} {r2=}")


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(Solution().findMedianSortedArrays(nums1, nums2))
    print(Solution().findMedianSortedArrays([], [1,2,3,4,5]))
    print(Solution().findMedianSortedArrays([1], [1]))
    print(Solution().findMedianSortedArrays([1,2], [-1,3]))
    print(Solution().findMedianSortedArrays([3,4], []), "===3.5")
