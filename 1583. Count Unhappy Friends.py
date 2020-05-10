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
    def unhappyFriends(
        self, n: int, preferences: List[List[int]], pairs: List[List[int]]
    ) -> int:
        can_cause_unhappy = [[] for _ in range(len(preferences))]

        for pair in pairs:
            for i in preferences[pair[0]]:
                if i != pair[1]:
                    can_cause_unhappy[pair[0]].append(i)
                else:
                    break
            for j in preferences[pair[1]]:
                if j != pair[0]:
                    can_cause_unhappy[pair[1]].append(j)
                else:
                    break

        print(f"{can_cause_unhappy=}")
        unhappy_count = 0
        for i in range(len(can_cause_unhappy)):
            for num in can_cause_unhappy[i]:
                if i in can_cause_unhappy[num]:
                    unhappy_count += 1
                    break

        return unhappy_count


if __name__ == "__main__":
    test(4, [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], [[0, 1], [2, 3]])
    test(2, [[1], [0]], [[1, 0]])
    test(4, [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], [[1, 3], [0, 2]])
