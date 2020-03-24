from typing import List


from collections import Counter
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for index in range(len(nums))[::-1]:
            if not index:
                break
            if nums[index-1] < nums[index]:
                to_replace_index = index - 1

                smallest = None
                smallest_value = nums[index-1]
                for finding_smallest in range(len(nums)-1, to_replace_index, -1):
                    if (not smallest or nums[smallest] > nums[finding_smallest]) and nums[finding_smallest] > smallest_value:
                        smallest = finding_smallest
                nums[to_replace_index], nums[smallest] = nums[smallest], nums[to_replace_index]
                print(f"{index=} {to_replace_index=} {smallest=}")
                nums[to_replace_index+1:] = list(reversed(nums[to_replace_index+1:]))
                print(nums)
                return
        nums.reverse()


def test(*args):
    print(f"{args=}", end="-->")
    s = Solution()
    ans = s.nextPermutation(*args)
    print("ans=", ans)
    print(*args)


if __name__ == "__main__":
    test([1,2,3])
    test([3,2,1])
    test([1,1,5])
    test([1,3,2])
    test([2,3,1])
