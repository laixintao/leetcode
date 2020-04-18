# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode, pre=None) -> ListNode:
        if not head: return pre
        next, head.next = head.next, pre
        return self.reverseList(next, head)
