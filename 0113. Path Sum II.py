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


class Solution:
    def search(self, node, sum, exists, current_sum, ans):
        # print(f"{current_sum=} {exists=} {node=}")
        current_sum += node.val
        exists = exists + [node.val]
        if current_sum == sum:
            # print(f"hit")
            if node.left is None and node.right is None:
                # print("append")
                ans.append(exists)
                return

        # print(f"{current_sum=} {exists=} {node=} {node.left=} {node.right=}")
        if node.left and node.left.val:
            # print(f"-> {node.left=}")
            self.search(node.left, sum, exists, current_sum, ans)
        if current_sum < sum and node.right and node.right.val:
            # print(f"-> {node.right=}")
            self.search(node.right, sum, exists, current_sum, ans)

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root or not root.val:
            return []
        ans = []
        self.search(root, sum, [], 0, ans)
        return ans


def test(*args):
    # print(f"{args=}")
    s = Solution()
    ans = s.pathSum(*args)
    # print("ans=", ans)


if __name__ == "__main__":
    root = create_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    test(root, 22)
