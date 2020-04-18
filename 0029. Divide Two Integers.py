class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = (dividend >= 0) != (divisor >= 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        ans = 0
        while dividend >= divisor:
            current_divisor = divisor
            unit = 1
            while dividend >= current_divisor:
                dividend -= current_divisor
                ans += unit

                current_divisor <<= 1
                unit <<= 1
        if negative:
            ans = -ans
        return max(min(ans, 2 ** 31 - 1), -(2 ** 31))


def test(*args):
    s = Solution()
    ans = s.divide(*args)
    print(args, "ans=", ans)


if __name__ == "__main__":
    test(15, 3)
    test(19, 9)
    test(-19, 9)
    test(19, -9)
    test(-19, -9)
    test(20, 5)
    test(3, 1)
