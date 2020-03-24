from typing import List


"""
动态规划
"""
from collections import Counter
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        longest_before = [0] * (len(s) + 1)

        for index in range(len(s)):
            if s[index] == "(":
                stack.append(index)
            else:
                if stack:
                    matched = stack.pop()
                    longest_before[index+1] = (index - matched + 1) + longest_before[matched]
        return max(longest_before)


def test(*args):
    print(f"{args=}", end="-->")
    s = Solution()
    ans = s.longestValidParentheses(*args)
    print("ans=", ans)


if __name__ == "__main__":
    test("(()")
    test(")()())")
    test("()(()")
    test("(()")
