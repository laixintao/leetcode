def find(nums):
    x = 0
    for num in nums:
        x ^= num
    for index in range(1, len(nums) + 2):
        x ^= index
    return x


def test(*args):
    ans = find(*args)
    print(f"{args=} {ans=}")


test([4, 3, 2, 1, 7, 5])
