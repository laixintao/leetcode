class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if head.next is None:
            return head
        total = 1

        tail = head
        while tail.next:
            total += 1
            tail = tail.next

        if k % total == 0:
            return head

        rotate = total - k % total - 1

        counter = head
        while rotate:
            counter = counter.next
            rotate -= 1

        new_head = counter.next
        counter.next = None
        tail.next = head
        return new_head
