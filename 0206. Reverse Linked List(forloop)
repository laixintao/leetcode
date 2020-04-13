# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        next = None
        current = head
        pre = None
        while current:
            next = current.next
            current.next = pre
            pre = current
            current = next
        return pre
