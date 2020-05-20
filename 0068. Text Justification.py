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
    def make_line(self, line, maxWidth):
        if (len(line)) == 1:
            return line[0] + " " * (maxWidth - len(line[0]))
        gap = len(line) - 1
        extra_spaces = maxWidth - sum(len(word) for word in line)
        spaces_between_words = extra_spaces // gap
        left_spaces = extra_spaces - spaces_between_words * gap
        # print(f"{extra_spaces=} {spaces_between_words=} {first_spaces=}")
        line_str = ""
        for i in range(len(line)):
            if i == 0:
                line_str += line[i]
            else:
                line_str += " " * spaces_between_words + " " * (left_spaces > 0) + line[i]
                left_spaces -= 1
        return line_str

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        i = 0
        line = []
        while i < len(words):
            if not line:
                line.append(words[i])
                i += 1
                continue
            if len(" ".join(line)) + len(words[i]) + 1 <= maxWidth:
                line.append(words[i])
                i += 1
                continue
            ans.append(self.make_line(line, maxWidth))
            line = []
        if line:
            last_line = " ".join(line)
            ans.append(last_line + " " * (maxWidth - len(last_line)))

        return ans


if __name__ == "__main__":
    test(["This", "is", "an", "example", "of", "text", "justification."], 16)
    test(["What", "must", "be", "acknowledgment", "shall", "be"], 16)
    test(
        [
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
        20,
    )
