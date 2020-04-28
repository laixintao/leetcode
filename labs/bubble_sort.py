def sort(nums):
    for end in range(len(nums) - 1, 0, -1):
        for index in range(end):
            if nums[index] > nums[index + 1]:
                nums[index + 1], nums[index] = nums[index], nums[index + 1]
    return nums


def test(nums):
    print(f"=> {nums}")
    sort(nums)
    print(f"<= {nums}")


test([4, 5, 6, 2, 1, 1, 3, 4, 6, 8, 9])
