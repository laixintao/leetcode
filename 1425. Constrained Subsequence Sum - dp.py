from typing import List
from collections import Counter, defaultdict
import bisect
import itertools


def create_tree(values):
    root = TreeNode(values.pop(0))
    roots = [root]
    while values:
        left, right = values.pop(0), values.pop(0)
        node = roots.pop(0)
        node.left = TreeNode(left)
        node.right = TreeNode(right)
        roots.extend([node.left, node.right])
    return root


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f"[{self.val}]({self.left}, {self.right})"

    def __repr__(self):
        return f"TreeNode({self.val})"


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


case = 0


def test(*args):
    global case
    print(f"---case {case}---")
    case += 1
    print(f"{args=}")
    s = Solution()
    ans = s.constrainedSubsetSum(*args)
    print("ans=", ans)


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        from collections import deque

        # dp[n] is number n must included
        dp = [0] * (len(nums) + 1)
        window = deque(maxlen=k)
        current_max = 0

        for index in range(1, len(nums) + 1):
            if len(window) < k:
                window.append(dp[index - 1])
            else:
                if dp[index - 1] >= current_max:
                    window.popleft()
                    window.append(dp[index - 1])
                else:
                    last = window.popleft()
                    window.append(dp[index - 1])
                    if last == current_max:
                        current_max = max(0, max(window))
            current_max = max(current_max, dp[index - 1])
            dp[index] = current_max + nums[index - 1]
            print(f"{index=} {window=} {nums[index-1]=} {current_max=}")
        print(dp)
        return max(dp[1:])


if __name__ == "__main__":
    test([10, 2, -10, 5, 20], 2)
    test([-1, -2, -3], 1)
    test([4681, 6466, 9411, -5130, 6047], 3)
    test([-8269, 3217, -4023, -4138, -683, 6455, -3621, 9242, 4015, -3790], 1)
