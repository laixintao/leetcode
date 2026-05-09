class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        low = 1
        high = x
        ans = 0
        while low <= high:
            current = ( low + high ) // 2

            if current ** 2 <= x:
                ans = current
                low = current + 1
            else:
                high = current - 1
        return ans

            



print(Solution().mySqrt(4))
print(Solution().mySqrt(8))
