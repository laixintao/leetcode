from typing import List  # noqa


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

# ---------
import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dis = defaultdict(dict)

        for t in times:
            start, end, cost = t
            dis[start-1][end-1] = cost

        visited = [False] * n

        cost_k = [float("inf")] * n
        cost_k[k-1] = 0
        unvisited = [(0, k-1)]

        while unvisited:
            _, current = heapq.heappop(unvisited)
            self.visit(current, dis, cost_k, visited, unvisited)

        total = max(cost_k)
        if total == float("inf"):
            return -1
        return int(total)

    def visit(self, current, dis, cost_k, visited, unvisited):
        if visited[current]:
            return

        for end, cost in dis[current].items():
            if cost_k[end] > cost_k[current] + cost:
                cost_k[end] = cost_k[current] + cost
                heapq.heappush(unvisited, (cost_k[end], end))

        visited[current] = True


if __name__ == "__main__":
    test(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2)
    test(times = [[1,2,1]], n = 2, k = 2)
