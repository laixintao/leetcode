from typing import List
from collections import Counter, defaultdict
import bisect
import itertools


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return f"[{self.val}]({self.left}, {self.right})"


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


import bisect


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        starts = []
        ends = []
        for pair in intervals:
            starts.append(pair[0])
            ends.append(pair[1])

        start, end = newInterval
        start_insert = bisect.bisect_left(ends, start)
        end_insert = bisect.bisect_right(starts, end)
        print(f"{start_insert=} {end_insert=}")
        # merge (start_insert, end_insert)
        starts[start_insert:end_insert] = [
            min(starts[start_insert:end_insert] + [start])
        ]
        ends[start_insert:end_insert] = [max(ends[start_insert:end_insert] + [end])]
        print(f"{starts=} {ends=}")
        return list(zip(starts, ends))


def test(*args):
    print(f"{args=}")
    s = Solution()
    ans = s.insert(*args)
    print("ans=", ans)


if __name__ == "__main__":
    test([[1,3],[6,9]],  [2,5])
