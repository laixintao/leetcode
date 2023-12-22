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
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = ord(target)
        if ord(letters[-1]) <= n:
            return letters[0]

        left, right = 0, len(letters)

        while left <= right:
            mid = int((left + right) / 2)
            mid_v = ord(letters[mid])

            if mid_v <= n:
                left = mid + 1
            elif mid_v - n == 1:
                return letters[mid]
            else:
                if mid==0:
                    return letters[mid]

                if ord(letters[mid-1]) <= n:
                    return letters[mid]

                right = mid

        return letters[0]
            


if __name__ == "__main__":
    test(letters = ["c","f","j"], target = "a")
    test(letters = ["c","f","j"], target = "c")
    test(letters = ["x","x","y","y"], target = "z")
