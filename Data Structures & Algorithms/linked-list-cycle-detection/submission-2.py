# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f, s = head, head
        while f and s:
            if not f or not s:
                return False
            s = s.next
            f = f.next
            if not f:
                return False
            f = f.next
            if f == s:
                return True
        return False