from typing import List  # noqa
import math


class Solution:
    def grayCode(self, n: int) -> list[int]:
        result = [0]
        for i in range(n):

            for x in range(len(result)-1,-1,-1):
                result.append(result[x] | 1 << i)
        return result


case = 0


def test(*args, **kwargs):
    global case
    print(f"---case {case}---")
    case += 1
    print(f"{args=}, {kwargs}")
    s = Solution()
    # find solution method
    function = [method for method in dir(s) if not method.startswith("__")][0]
    ans = getattr(s, function)(*args, **kwargs)
    print("ans=", ans)


if __name__ == "__main__":
    test(4)
    test(2)
    test(3)
    test(1)
