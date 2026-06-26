# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = head
        if not head:
            return False
        p2 = head.next
        while True:
            if not p1 or not p2:
                return False
            if p1 == p2:
                return True
            if not p2.next or not p2.next.next:
                return False
            p2 = p2.next.next
            if not p1.next:
                return False
            p1 = p1.next