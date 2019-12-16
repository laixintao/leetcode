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
    ans = s.uniquePathsWithObstacles(*args)
    print("ans=", ans)


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 0 if obstacleGrid[0][0] else 1
        print(f"{m=} {n=} {dp[0][0]=}")

        for i in range( m):
            for j in range( n):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    if i >=1:
                        dp[i][j] += dp[i - 1][j]
                    if j>=1:
                        dp[i][j] += dp[i][j-1]

                print(f"{i=} {j=} {dp[i][j]=}")
        return dp[-1][-1]


if __name__ == "__main__":
    test([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    test([[1,0]])
