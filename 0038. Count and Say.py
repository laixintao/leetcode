class Solution:
    def readoff(self, s):
        current = None
        count = 0
        ans = ""
        for char in s:
            if current == char:
                count += 1
            else:
                if count:
                    ans += str(count) + current
                current = char
                count = 1
        if count:
            ans += str(count) + current
        return ans

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.readoff(self.countAndSay(n - 1))


def test(*args):
    s = Solution()
    ans = s.countAndSay(*args)
    print(args, "ans=", ans)


if __name__ == "__main__":
    test(1)
    test(2)
    test(4)
