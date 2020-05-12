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
    # find solution method
    function = [method for method in dir(s) if not method.startswith("__")][0]
    ans = getattr(s, function)(*args)
    print("ans=", ans)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dis = []
        for i in range(len(points)):
            for j in range(i, len(points)):
                dis.append(
                    (
                        abs(points[i][0] - points[j][0])
                        + abs(points[i][1] - points[j][1]),
                        i,
                        j,
                    )
                )
        dis = sorted(dis, key=lambda x: x[0])

        joined = 1
        cost = 0
        parents = [x for x in range(len(points))]

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        for edge in dis:
            if find(edge[1]) != find(edge[2]):
                joined += 1
                cost += edge[0]
                parents[find(edge[1])] = edge[2]
            if joined == len(points):
                return cost


if __name__ == "__main__":
    test([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]])
    test(
        [
            [-8, 14],
            [16, -18],
            [-19, -13],
            [-18, 19],
            [20, 20],
            [13, -20],
            [-15, 9],
            [-4, -8],
        ]
    )
