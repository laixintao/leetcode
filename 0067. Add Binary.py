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
    ans = s.addBinary(*args)
    print("ans=", ans)


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        from itertools import zip_longest

        carry = False
        ans = []
        for i, j in zip_longest(reversed(a), reversed(b)):
            if not i:
                ans.append(j)
            elif not j:
                ans.append(i)
            else:
                temp = int(i) + int(j) + carry
                if temp == 3:
                    ans.append(1)
                elif temp == 2:
                    carry = True
                    ans.append(0)
                elif temp == 1:
                    carry = False
                    ans.append(1)
                else:
                    carry = False
                    ans.append(0)
        if carry:
            ans.append(1)
        return "".join([str(x) for x in reversed(ans)])


if __name__ == "__main__":
    test("1010", "1011")
    test("1010", "10110")
