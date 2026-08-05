# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        c = head
        while c:
            l += 1
            c = c.next
        if l == 1:
            head = None
            return head
        if l == n:
            head = head.next
            return head
        first, second = head, head.next
        while l - n - 1 > 0:
            l -= 1
            first, second = first.next, second.next
        first.next = second.next # remove second
        return head
            